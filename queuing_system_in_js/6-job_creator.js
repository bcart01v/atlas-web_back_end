import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
    phoneNumber: '1234567890',
    message: 'This is the code to verify your account'
};

const job = queue.create('push_notification_code', jobData)
    .save((err) => {
        if (!err) {
            console.log(`Notification job created: ${job.id}`);
        }
    });

job.on('complete', () => {
    console.log('Notification job completed');
});

job.on('failed', () => {
    console.log('Notificaion job failed');
});