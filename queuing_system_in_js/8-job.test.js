import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should display an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should not create any jobs if an empty array is passed', () => {
    createPushNotificationsJobs([], queue);
    expect(queue.testMode.jobs.length).to.equal(0);
  });

  it('should throw an error if jobs is undefined', () => {
    expect(() => createPushNotificationsJobs(undefined, queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should throw an error if jobs is null', () => {
    expect(() => createPushNotificationsJobs(null, queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should throw an error if jobs is an object', () => {
    expect(() => createPushNotificationsJobs({ phoneNumber: '4153518780', message: 'Test' }, queue)).to.throw(Error, 'Jobs is not an array');
  });
});