# Developer Assignment CruzHacks 2019

######

Hi CruzHacks team! I'm super stoked by the chance to help to contribute to CruzHacks 2019. I think CruzHack's aim to promote inclusion in tech is fantastic and I want to help! Here is my crack at the developer assignment. I had a bunch of fun working on it!

######

### How to run
- The api is wrapped inside two docker container orchestrated using docker-compose. You will need to have Docker installed on your system. To run, cd to the root directory of the project and run `docker-compose up`. This will build and launch the Docker containers.

### Note
- I've found that campus wifi can block the connection to the MongoDB databse. If so, you will either have to run on a VPN or a private network.
- The entire project uses about 480 mb and takes ~2 minutes to build.

######

### Example
`curl -XGET -H ‘Content-Type: application/json’ http://localhost:300/hackers/1`

```javascript
{
  "code": "200",
  "message": "Hacker retrieved successfully.",
  "results": {
    "college": "UCSC",
    "created_at": "2018-05-19 04:51:07",
    "email": "sslug@ucsc.edu",
    "id": 1,
    "last_updated_at": "2018-05-19 04:51:07",
    "major": "Graphic Design",
    "name": "Sammy Slug"
  }
}
```

######

### Developed With
  - Python
    - Flask
    - Packages
        - Flask == 1.0
        - names == 0.3.0
        - pymongo == 3.6.1
        - pytest
  - Databse
    - MongoDB
        - MLab
- Docker
    - Docker Compose


######

### Links
  - [Kyle O'Brien Linkedin](https://www.linkedin.com/in/kyle1668)
