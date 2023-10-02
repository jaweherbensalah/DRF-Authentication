# Debugging Jobs in GitLab CI
## Setting up a Docker runner

```
$ sudo apt update
```

```
$ curl -LJO https://gitlab-runner-downloads.s3.amazonaws.com/latest/deb/gitlab-runner_amd64.deb
```

```
$ sudo dpkg -i gitlab-runner_amd64.deb
```
```
$ sudo gitlab-runner start
```
Runtime platform                                    arch=amd64 os=linux pid=35796 revision=6e766faf version=16.4.0
```
$ sudo gitlab-runner status
```
Runtime platform                                    arch=amd64 os=linux pid=36352 revision=6e766faf version=16.4.0
gitlab-runner: Service is running


### Register a Docker runner so you can run a job locally 

```
$ sudo gitlab-runner register 
```

Runtime platform                                    arch=amd64 os=linux pid=38852 revision=6e766faf version=16.4.0
Running in system-mode.                            
                                                   
Enter the GitLab instance URL (for example, https://gitlab.com/):

https://gitlab.com

Enter the registration token:

[YOUR TOKEN]

Enter a description for the runner:
```
debugging
```
Enter tags for the runner (comma-separated):
```
debugging
```
Enter optional maintenance note for the runner:

WARNING: Support for registration tokens and runner parameters in the 'register' command has been deprecated in GitLab Runner 15.6 and will be replaced with support for authentication tokens. For more information, see https://docs.gitlab.com/ee/ci/runners/new_creation_workflow 



Registering runner... succeeded                     runner=[...]


** Enter an executor: ssh, virtualbox, docker-autoscaler, docker+machine, custom, docker, docker-windows, parallels, shell, instance, kubernetes:
```
docker
```
Enter the default Docker image (for example, ruby:2.7):
```
python:3.8
```

Runner registered successfully. Feel free to start it, but if it's running already the config should be automatically reloaded!
 
Configuration (with the authentication token) was saved in "/etc/gitlab-runner/config.toml" 
```
$ sudo gitlab-runner verify
```

Runtime platform                                    arch=amd64 os=linux pid= revision= version=16.4.0
Running in system-mode.                            
                                                   
**Verifying runner... is alive                        runner= ..**

```
gitlab-runner list
```
## Execute a GitLab CI/CD job locally using the gitlab-runner exec docker command 
### Add a gitalb-ci.yml file with some jobs

### Adjusting jobs so they can run locally

 This is the command to run the job to debug:


```
$ gitlab-runner exec docker build-job
```

**Job succeeded**

![](https://gitlab.com/jaweherbensalah/DRF_Authentication/-/raw/master/Screenshot_from_2023-09-28_07-02-50.png?ref_type=heads)

```
$ gitlab-runner exec docker unit-test-job
```

**Job failed**



 ## Access the Docker container running the job for debugging purposes
``` 
$ docker ps
```

CONTAINER ID    5e185a3cfb95          
IMAGE           8ca4688f4f35                 
COMMAND         "sh -c 'if [ -x /usr…"   
CREATED         4 seconds ago   
STATUS          Up 3 seconds  
PORTS                                      
NAMES           runner--project-0-concurrent-0-02aba32703244a96-build

```
docker exec -it runner--project-0-concurrent-0-8ef7d674b79ffcff-build  ash
```

Once in the container, you'll need to locate the source code. GitLab Runner creates a directory called builds at the root of the container’s file system. Once there, you can see your project files and you're ready to debug the failing job:

```
$ docker exec -it runner--project-0-concurrent-0-a5ee1e548d3130ec-build ash
/ # ls
bin     dev     home    media   opt     root    sbin    sys     usr
builds  etc     lib     mnt     proc    run     srv     tmp     var
/ # pwd
/
/ # cd home
/home # ls
user
/home # cd user
/home/user # ls
Desktop
/home/user # cd Desktop 
/home/user/Desktop # ls
Projects
/home/user/Desktop # cd Projects
/home/user/Desktop/Projects # ls
auth
/home/user/Desktop/Projects # cd auth 
/home/user/Desktop/Projects/auth # ls
manage.py
accounts                                 readme.md
auth                                     requirements.txt
builds                                   social_auth
db.sqlite3                               templates
env                                      translation
locale

/home/user/Desktop/Projects/auth # cd /builds/
/builds # cd project-0
/builds/project-0 # ls
manage.py
accounts                                 readme.md
auth                                     requirements.txt
builds                                   social_auth
db.sqlite3                               translation
locale
/builds/project-0 # 

```
## Next steps

1. **Debug the Job**: Now that you have accessed the Docker container running the job, you can navigate to the project directory and inspect the files and logs to debug any issues. In your case, you already located the project files using the `ls` command and found the source code.

2. **Identify and Fix Issues**: Look for any error messages, logs, or issues within the container that may have caused the job to fail or behave unexpectedly. 

3. **Make Necessary Corrections**: Once you have identified the issue, make the necessary corrections to your project files or configuration within the Docker container. In many cases, you might need to adjust your `.gitlab-ci.yml` file or other project-specific settings.

4. **Test and Re-run**: After making corrections, you can test your changes within the Docker container to ensure that the issue has been resolved. If you're confident that the problem is fixed, you can exit the Docker container and re-run the job using `gitlab-runner exec docker` to confirm that it completes successfully.

5. **Commit and Push Changes**: If everything works as expected, commit the changes you made during debugging to your project repository. Once the changes are committed, you can push them to your remote repository on GitLab.

6. **Monitor the CI/CD Pipeline**: After pushing the changes, monitor your GitLab CI/CD pipeline on GitLab's web interface. Check if the pipeline runs successfully with the corrected configuration. If it does, you've successfully resolved the issue.

7. **Continuous Improvement**: Continue to use GitLab CI/CD for automated testing, building, and deploying your project. As you make code changes, ensure that your CI/CD pipeline runs smoothly to maintain code quality and reliability.


## Conclusion


Here are a couple of points for you to take with you the next time a GitLab CI job does not work as expected:

- Register a Docker runner for the repository that you are working with. 

- Check out the unsupported features when running jobs via gitlab-runner exec. Adjust the job accordingly.

- Add a sleep 1h statement where you want the job to halt when it runs. Commit that, but don’t push it.

- Run the job with the command gitlab-runner exec docker [job id goes here].