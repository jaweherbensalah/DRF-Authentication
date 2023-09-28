# Debugging Jobs in GitLab CI
### Setting up a Docker runner

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

Runtime platform                                    arch=amd64 os=linux pid=40990 revision=6e766faf version=16.4.0
Running in system-mode.                            
                                                   
**Verifying runner... is alive                        runner= ..**


# Add a gitalb-ci.yml file with some jobs

# Adjusting jobs so they can run locally

 This is the command to run the job to debug:


```
$ gitlab-runner exec shell build-job
```

**Job succeeded**

![](https://gitlab.com/jaweherbensalah/DRF_Authentication/-/blob/master/Screenshot_from_2023-09-28_07-02-50.png)


