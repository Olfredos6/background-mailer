[![initial-workflow](https://github.com/Olfredos6/background-mailer/actions/workflows/init.yaml/badge.svg?event=push)](https://github.com/Olfredos6/background-mailer/actions/workflows/init.yaml)

# background-mailer
A python service used to send emails
**Note that this service can face the internet but I recommend it remains for internal use**


### Using the service for free
There is an AWS instace of the service running on at nehemie.dev/api/mailer. Please note that service's availability is not guaranteed at the moment. 
### Deplyoying the service yourself
System Requirements:

 - Git
 - Docker

You would start by cloning the repository to your sever. Then CD into the repo's folder and start it using *docker run* as follows:
`docker run [-d, --rm, -e] [--name some-name] -p IN[:OUT] -v /absolute/path/to/folder`

## How it works
The system is a django project with 2 applications:
- Core: Used to compose and send emails
- API: used interface with the core application
At the moment, the API only  responds to a POST request to the / route to post an email. 

### Request payload
Below is a sample payload:
POST /
```
    { 
    	"host": "mail.test.com",
    	"port": 465,
    	"username": "mail1@test.com",
    	"password": "some_password",
    	"subject": "Testing",
    	"recipient": "mail2@test.com",
    	"message": "Message content",
    	"html": true
    }
```
#### Required parameters
At firt, the Core application will try to use values specified in the request to configure the SMTP client. If the payload does not specify any of **host**, **port**, **username**, or **password**, the system will try to use the values defined in the environment variables. You must execute `docker run` with the -e option to specify the environemnt values. The required environment values are: BKG_MAIL_HOST,  BKG_MAIL_PORT, BKG_MAIL_USERNAME, and BKG_MAIL_PASSWORD.

The payload must include:
- subject: subject of the email
- recipient: scalar or list of recipient emails
- message: message content

#### Non-required parameters**
The **html** property is used to indicate that the should be constructed as a multipart/alternative, a.k.a, an HTML message.
