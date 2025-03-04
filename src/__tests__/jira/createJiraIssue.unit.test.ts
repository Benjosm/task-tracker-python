// src/__tests__/jira/createJiraIssue.unit.test.ts
import { describe, it, expect, vi, type Mock } from 'vitest';

// Create a mock for the addNewIssue method.
const addNewIssueMock = vi.fn();

// 1. Mock the entire 'jira-client' module.
vi.mock('jira-client', () => {
  return {
    __esModule: true,
    default: vi.fn().mockImplementation(() => ({
      addNewIssue: addNewIssueMock,
    })),
  };
});

import JiraClient from 'jira-client';
import { createJiraIssue } from 'src/jira_functions/createIssue';


describe('createJiraIssue', () => {

  it('should create an issue successfully with valid fields', async () => {
    // Arrange
    const params = {
      jiraBaseUrl: 'https://example.atlassian.net/', // trailing slash will be normalized
      username: 'user@example.com',
      password: 'apiToken',
      fields: {
        project: { key: 'TEST' },
        issuetype: { name: 'Story' },
        summary: 'An example issue',
        description: 'Detailed description here',
        customfield_12345: 5,
      },
    };

    const fakeIssue = { id: '10001', key: 'TEST-10001' };
    addNewIssueMock.mockResolvedValueOnce(fakeIssue);

    // Act
    const result = await createJiraIssue(params);

    // Assert

    // Verify that JiraClient was initialized with the correct parameters.
    const mockedJiraClient = JiraClient as unknown as Mock;
    expect(mockedJiraClient).toHaveBeenCalledTimes(1);
    expect(mockedJiraClient).toHaveBeenCalledWith({
      protocol: 'https',
      host: 'example.atlassian.net', // trailing slash removed
      username: params.username,
      password: params.password,
      apiVersion: '2',
      strictSSL: false, // as specified in the function
    });

    // Verify that addNewIssue was called with the correct payload.
    expect(addNewIssueMock).toHaveBeenCalledTimes(1);
    expect(addNewIssueMock).toHaveBeenCalledWith({ fields: params.fields });

    // Verify the function returns the created issue.
    expect(result).toEqual(fakeIssue);
  });

  it('should throw an error if project.key is missing', async () => {
    // Arrange: Missing project.key in the fields.
    const params = {
      jiraBaseUrl: 'https://example.atlassian.net',
      username: 'user@example.com',
      password: 'apiToken',
      fields: {
        project: {},
        issuetype: { name: 'Story' },
        summary: 'An example issue',
      },
    };

    // Act & Assert
    await expect(createJiraIssue(params)).rejects.toThrow('Missing required field: project.key');
  });

  it('should throw an error if issuetype (name or id) is missing', async () => {
    // Arrange: Missing issuetype name and id.
    const params = {
      jiraBaseUrl: 'https://example.atlassian.net',
      username: 'user@example.com',
      password: 'apiToken',
      fields: {
        project: { key: 'TEST' },
        issuetype: {},
        summary: 'An example issue',
      },
    };

    // Act & Assert
    await expect(createJiraIssue(params)).rejects.toThrow('Missing required field: issuetype (name or id)');
  });

  it('should throw an error if summary is missing', async () => {
    // Arrange: Missing summary in the fields.
    const params = {
      jiraBaseUrl: 'https://example.atlassian.net',
      username: 'user@example.com',
      password: 'apiToken',
      fields: {
        project: { key: 'TEST' },
        issuetype: { name: 'Story' },
        // summary is omitted
      },
    };

    // Act & Assert
    await expect(createJiraIssue(params)).rejects.toThrow('Missing required field: summary');
  });

  it('should throw an error when addNewIssue fails', async () => {
    // Arrange
    const params = {
      jiraBaseUrl: 'https://example.atlassian.net/',
      username: 'user@example.com',
      password: 'apiToken',
      fields: {
        project: { key: 'TEST' },
        issuetype: { name: 'Story' },
        summary: 'An example issue',
      },
    };

    const error = new Error('API failure');
    addNewIssueMock.mockRejectedValueOnce(error);

    // Act & Assert
    await expect(createJiraIssue(params)).rejects.toThrow(`Error creating Jira issue: ${error}`);
    expect(addNewIssueMock).toHaveBeenCalledTimes(1);
  });

  it('should create a Task issue in TM project with required fields', async () => {
    // Arrange
    const params = {
      jiraBaseUrl: 'https://example.atlassian.net/',
      username: 'user@example.com',
      password: 'apiToken',
      fields: {
        project: { key: 'TM' },
        issuetype: { name: 'Task' },
        summary: 'Test Task for TM-105',
      },
    };

    const fakeIssue = { id: '10002', key: 'TM-105' };
    addNewIssueMock.mockResolvedValueOnce(fakeIssue);

    // Act
    const result = await createJiraIssue(params);

    // Assert
    expect(result).toEqual(fakeIssue);

    const mockedJiraClient = JiraClient as unknown as Mock;
    expect(mockedJiraClient).toHaveBeenCalledTimes(1);
    expect(mockedJiraClient).toHaveBeenCalledWith({
      protocol: 'https',
      host: 'example.atlassian.net',
      username: params.username,
      password: params.password,
      apiVersion: '2',
      strictSSL: false,
    });

    expect(addNewIssueMock).toHaveBeenCalledTimes(1);
    expect(addNewIssueMock).toHaveBeenCalledWith({ fields: params.fields });
  });

  it('should throw an error if jiraBaseUrl is missing', async () => {
    // Arrange: Missing jiraBaseUrl in the params.
    const params = {
      username: 'user@example.com',
      password: 'apiToken',
      fields: {
        project: { key: 'TEST' },
        issuetype: { name: 'Story' },
        summary: 'An example issue',
      },
    };

    // Act & Assert
    await expect(createJiraIssue(params)).rejects.toThrow('jiraBaseUrl is required');
  });

  it('should throw an error if jiraBaseUrl is invalid format', async () => {
    // Arrange: Invalid jiraBaseUrl format in the params.
    const params = {
      jiraBaseUrl: 'example.atlassian.net', // Missing protocol (http:// or https://)
      username: 'user@example.com',
      password: 'apiToken',
      fields: {
        project: { key: 'TEST' },
        issuetype: { name: 'Story' },
        summary: 'An example issue',
      },
    };

    // Act & Assert
    await expect(createJiraIssue(params)).rejects.toThrow('Invalid jiraBaseUrl format. It must start with http:// or https://');
  });
});
