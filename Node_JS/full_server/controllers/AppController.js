// This is the App Controller

class AppController {
    static getHomepage(req, res) {
        res.status(200).send('Hello Atlas School!');
    }
}

export default AppController;