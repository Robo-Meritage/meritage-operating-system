#!/usr/bin/env python3
"""Mirror the repo's Markdown docs into a Google Drive folder (one-way sync).

Runs in GitHub Actions. Requires two repository secrets:
  GDRIVE_SERVICE_ACCOUNT_JSON - the service account key JSON
  GDRIVE_FOLDER_ID            - the target Drive folder ID

Each doc is tagged in Drive with its repo path, so re-runs UPDATE the same
file instead of making duplicates. Docs removed from the repo are moved to
the Drive trash, so the folder always matches the repo.
"""
import os
import io
import json
import glob

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

SCOPES = ["https://www.googleapis.com/auth/drive"]


def main():
    info = json.loads(os.environ["GDRIVE_SERVICE_ACCOUNT_JSON"])
    creds = service_account.Credentials.from_service_account_info(info, scopes=SCOPES)
    drive = build("drive", "v3", credentials=creds)
    folder = os.environ["GDRIVE_FOLDER_ID"]

    # Files to mirror: key root docs + everything under docs/
    paths = [p for p in ["CLAUDE.md", "AGENTS.md", "CONTRIBUTING.md"] if os.path.isfile(p)]
    paths += sorted(glob.glob("docs/**/*.md", recursive=True))

    seen = set()
    for path in paths:
        if os.path.getsize(path) <= 60:
            continue  # skip empty placeholder files
        seen.add(path)

        with open(path, "rb") as fh:
            media = MediaIoBaseUpload(io.BytesIO(fh.read()), mimetype="text/markdown")

        safe = path.replace("'", "\\'")
        q = "appProperties has {key='repoPath' and value='%s'} and trashed=false" % safe
        found = drive.files().list(
            q=q, spaces="drive", fields="files(id)"
        ).execute().get("files", [])

        if found:
            drive.files().update(fileId=found[0]["id"], media_body=media).execute()
            print("updated", path)
        else:
            body = {"name": path, "parents": [folder], "appProperties": {"repoPath": path}}
            drive.files().create(body=body, media_body=media, fields="id").execute()
            print("created", path)

    # Move to trash any Drive doc whose source file no longer exists in the repo
    q = "appProperties has {key='repoPath'} and '%s' in parents and trashed=false" % folder
    for f in drive.files().list(
        q=q, spaces="drive", fields="files(id,appProperties)"
    ).execute().get("files", []):
        rp = (f.get("appProperties") or {}).get("repoPath")
        if rp and rp not in seen:
            drive.files().update(fileId=f["id"], body={"trashed": True}).execute()
            print("removed", rp)

    print("Sync complete:", len(seen), "files")


if __name__ == "__main__":
    main()
