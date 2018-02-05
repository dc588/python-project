pipeline{
  agent none

  stages{
    stage ('python-project'){
      agent any
      steps{
        sh 'python newfile.py'
          echo "ID"
          sh 'id'
          echo "PWD"
          sh 'pwd'
      }
    }

    stage ('sayHello'){
      agent any
      steps{
        sayHello 'Brent'
      }
    }

    stage('merge development to master'){
      agent any
      when{
        branch 'development'
      }

      steps{
        echo "Stashing any local changes"
        sh 'git stash'
        echo "checkout development"
        sh 'git checkout development'
        echo "pull latest changes"
        sh 'git pull'
        echo "checkout master"
        sh 'git checkout master'
        echo "pull latest from master"
        sh 'git pull'
        echo "merging development into master"
        sh 'git merge development'
        echo "Pushing to remote"
        sh 'git push origin master'
      }
    }

    stage('promote to green'){
      agent{
        label 'apache'
      }
      when{
        branch 'development'
      }
      steps{

        sh 'if [ ! -d '/var/www/html/green']';then echo "It does not exist";fi
      }
    }
  }
}
