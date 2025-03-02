import pytest
import json


def test_jira_issue_creation():
    jira_payload_str = '''
{
  "timestamp": 1740947640940,
  "webhookEvent": "jira:issue_created",
  "issue_event_type_name": "issue_created",
  "user": {
    "self": "https://aisoftdev.atlassian.net/rest/api/2/user?accountId=712020%3Ac9deea9c-b204-4bdb-9e10-8fc5837c0831",
    "accountId": "712020:c9deea9c-b204-4bdb-9e10-8fc5837c0831",
    "avatarUrls": {
      "48x48": "https://secure.gravatar.com/avatar/b864793b20f3a92143af65c7620cb19f?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBM-0.png",
      "24x24": "https://secure.gravatar.com/avatar/b864793b20f3a92143af65c7620cb19f?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBM-0.png",
      "16x16": "https://secure.gravatar.com/avatar/b864793b20f3a92143af65c7620cb19f?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBM-0.png",
      "32x32": "https://secure.gravatar.com/avatar/b864793b20f3a92143af65c7620cb19f?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBM-0.png"
    },
    "displayName": "Benjamin Moen",
    "active": true,
    "timeZone": "America/Chicago",
    "accountType": "atlassian"
  },
  "issue": {
    "id": "10411",
    "self": "https://aisoftdev.atlassian.net/rest/api/2/10411",
    "key": "TM-100",
    "fields": {
      "statuscategorychangedate": "2025-03-02T14:34:00.965-0600",
      "issuetype": {
        "self": "https://aisoftdev.atlassian.net/rest/api/2/issuetype/10017",
        "id": "10017",
        "description": "Tasks track small, distinct pieces of work.",
        "iconUrl": "https://aisoftdev.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10318?size=medium",
        "name": "Task",
        "subtask": false,
        "avatarId": 10318,
        "entityId": "d6f4dfe4-5995-4b80-ad8e-49a14c0df13b",
        "hierarchyLevel": 0
      },
      "timespent": null,
      "customfield_10030": null,
      "project": {
        "self": "https://aisoftdev.atlassian.net/rest/api/2/project/10003",
        "id": "10003",
        "key": "TM",
        "name": "Task Tracker Python",
        "projectTypeKey": "software",
        "simplified": true,
        "avatarUrls": {
          "48x48": "https://aisoftdev.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10403",
          "24x24": "https://aisoftdev.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10403?size=small",
          "16x16": "https://aisoftdev.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10403?size=xsmall",
          "32x32": "https://aisoftdev.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10403?size=medium"
        }
      },
      "customfield_10031": null,
      "fixVersions": [],
      "customfield_10034": null,
      "aggregatetimespent": null,
      "resolution": null,
      "customfield_10035": null,
      "customfield_10036": null,
      "customfield_10027": null,
      "customfield_10028": null,
      "customfield_10029": null,
      "resolutiondate": null,
      "workratio": -1,
      "issuerestriction": {
        "issuerestrictions": {},
        "shouldDisplay": true
      },
      "lastViewed": null,
      "watches": {
        "self": "https://aisoftdev.atlassian.net/rest/api/2/issue/TM-100/watchers",
        "watchCount": 0,
        "isWatching": true
      },
      "created": "2025-03-02T14:34:00.631-0600",
      "customfield_10020": null,
      "customfield_10021": null,
      "customfield_10022": null,
      "priority": {
        "self": "https://aisoftdev.atlassian.net/rest/api/2/priority/3",
        "iconUrl": "https://aisoftdev.atlassian.net/images/icons/priorities/medium.svg",
        "name": "Medium",
        "id": "3"
      },
      "customfield_10023": null,
      "customfield_10024": null,
      "customfield_10025": null,
      "customfield_10026": null,
      "labels": [],
      "customfield_10016": null,
      "customfield_10017": null,
      "customfield_10018": {
        "hasEpicLinkFieldDependency": false,
        "showField": false,
        "nonEditableReason": {
          "reason": "EPIC_LINK_SHOULD_BE_USED",
          "message": "To set an epic as the parent, use the epic link instead"
        }
      },
      "customfield_10019": "0|i000d3:",
      "timeestimate": null,
      "aggregatetimeoriginalestimate": null,
      "versions": [],
      "issuelinks": [],
      "assignee": null,
      "updated": "2025-03-02T14:34:00.631-0600",
      "status": {
        "self": "https://aisoftdev.atlassian.net/rest/api/2/status/10009",
        "description": "",
        "iconUrl": "https://aisoftdev.atlassian.net/",
        "name": "To Do",
        "id": "10009",
        "statusCategory": {
          "self": "https://aisoftdev.atlassian.net/rest/api/2/statuscategory/2",
          "id": 2,
          "key": "new",
          "colorName": "blue-gray",
          "name": "New"
        }
      },
      "components": [],
      "timeoriginalestimate": null,
      "description": "The build logs for PR #22 appear clean, but the pull request failed to merge with the error 'Pull Request is not mergeable'. Please investigate why the PR is not mergeable and take appropriate actions.",
      "customfield_10010": null,
      "customfield_10014": null,
      "timetracking": {},
      "customfield_10015": null,
      "customfield_10005": null,
      "customfield_10006": null,
      "security": null,
      "customfield_10007": null,
      "customfield_10008": null,
      "customfield_10009": null,
      "aggregatetimeestimate": null,
      "attachment": [],
      "summary": "PR #22 Failed to Merge - Please Investigate",
      "creator": {
        "self": "https://aisoftdev.atlassian.net/rest/api/2/user?accountId=712020%3Ac9deea9c-b204-4bdb-9e10-8fc5837c0831",
        "accountId": "712020:c9deea9c-b204-4bdb-9e10-8fc5837c0831",
        "avatarUrls": {
          "48x48": "https://secure.gravatar.com/avatar/b864793b20f3a92143af65c7620cb19f?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBM-0.png",
          "24x24": "https://secure.gravatar.com/avatar/b864793b20f3a92143af65c7620cb19f?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBM-0.png",
          "16x16": "https://secure.gravatar.com/avatar/b864793b20f3a92143af65c7620cb19f?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBM-0.png",
          "32x32": "https://secure.gravatar.com/avatar/b864793b20f3a92143af65c7620cb19f?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBM-0.png"
        },
        "displayName": "Benjamin Moen",
        "active": true,
        "timeZone": "America/Chicago",
        "accountType": "atlassian"
      },
      "subtasks": [],
      "reporter": {
        "self": "https://aisoftdev.atlassian.net/rest/api/2/user?accountId=712020%3Ac9deea9c-b204-4bdb-9e10-8fc5837c0831",
        "accountId": "712020:c9deea9c-b204-4bdb-9e10-8fc5837c0831",
        "avatarUrls": {
          "48x48": "https://secure.gravatar.com/avatar/b864793b20f3a92143af65c7620cb19f?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBM-0.png",
          "24x24": "https://secure.gravatar.com/avatar/b864793b20f3a92143af65c7620cb19f?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBM-0.png",
          "16x16": "https://secure.gravatar.com/avatar/b864793b20f3a92143af65c7620cb19f?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBM-0.png",
          "32x32": "https://secure.gravatar.com/avatar/b864793b20f3a92143af65c7620cb19f?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBM-0.png"
        },
        "displayName": "Benjamin Moen",
        "active": true,
        "timeZone": "America/Chicago",
        "accountType": "atlassian"
      },
      "aggregateprogress": {
        "progress": 0,
        "total": 0
      },
      "customfield_10001": null,
      "customfield_10002": [],
      "customfield_10003": null,
      "customfield_10004": null,
      "environment": null,
      "duedate": null,
      "progress": {
        "progress": 0,
        "total": 0
      },
      "votes": {
        "self": "https://aisoftdev.atlassian.net/rest/api/2/issue/TM-100/votes",
        "votes": 0,
        "hasVoted": false
      }
    }
  },
  "changelog": {
    "id": "10518",
    "items": [
      {
        "field": "description",
        "fieldtype": "jira",
        "fieldId": "description",
        "from": null,
        "fromString": null,
        "to": null,
        "toString": "The build logs for PR #22 appear clean, but the pull request failed to merge with the error 'Pull Request is not mergeable'. Please investigate why the PR is not mergeable and take appropriate actions."
      },
      {
        "field": "priority",
        "fieldtype": "jira",
        "fieldId": "priority",
        "from": null,
        "fromString": null,
        "to": "3",
        "toString": "Medium"
      },
      {
        "field": "reporter",
        "fieldtype": "jira",
        "fieldId": "reporter",
        "from": null,
        "fromString": null,
        "to": "712020:c9deea9c-b204-4bdb-9e10-8fc5837c0831",
        "toString": "Benjamin Moen",
        "tmpFromAccountId": null,
        "tmpToAccountId": "712020:c9deea9c-b204-4bdb-9e10-8fc5837c0831"
      },
      {
        "field": "Status",
        "fieldtype": "jira",
        "fieldId": "status",
        "from": null,
        "fromString": null,
        "to": "10009",
        "toString": "To Do"
      },
      {
        "field": "summary",
        "fieldtype": "jira",
        "fieldId": "summary",
        "from": null,
        "fromString": null,
        "to": null,
        "toString": "PR #22 Failed to Merge - Please Investigate"
      }
    ]
  }
}
    '''
    jira_payload = json.loads(jira_payload_str)
    assert "webhookEvent" in jira_payload
    assert jira_payload["webhookEvent"] == "jira:issue_created"
    assert "issue_event_type_name" in jira_payload
    assert jira_payload["issue_event_type_name"] == "issue_created"
    assert "issue" in jira_payload
    assert "user" in jira_payload

    # Assertions for 'user' dictionary
    assert "accountId" in jira_payload["user"]
    assert jira_payload["user"]["accountId"] == "712020:c9deea9c-b204-4bdb-9e10-8fc5837c0831"
    assert "displayName" in jira_payload["user"]
    assert jira_payload["user"]["displayName"] == "Benjamin Moen"

    # Assertions for 'issue' dictionary
    assert "key" in jira_payload["issue"]
    assert jira_payload["issue"]["key"] == "TM-100"
    assert "fields" in jira_payload["issue"]
    assert "summary" in jira_payload["issue"]["fields"]
    assert jira_payload["issue"]["fields"]["summary"] == "PR #22 Failed to Merge - Please Investigate"
    assert "description" in jira_payload["issue"]["fields"]
    assert jira_payload["issue"]["fields"]["description"] == "The build logs for PR #22 appear clean, but the pull request failed to merge with the error 'Pull Request is not mergeable'. Please investigate why the PR is not mergeable and take appropriate actions."
    assert "project" in jira_payload["issue"]["fields"]
    assert jira_payload["issue"]["fields"]["project"]["key"] == "TM"
    assert "issuetype" in jira_payload["issue"]["fields"]
    assert jira_payload["issue"]["fields"]["issuetype"]["name"] == "Task"
    assert jira_payload["issue"]["fields"]["issuetype"]["id"] == "10017" # Asserting issuetype id
    assert jira_payload["issue"]["fields"]["status"]["name"] == "To Do"
    assert jira_payload["issue"]["fields"]["status"]["id"] == "10009" # Asserting status id
    assert jira_payload["issue"]["fields"]["priority"]["name"] == "Medium"
    assert jira_payload["issue"]["fields"]["priority"]["id"] == "3" # Asserting priority id

