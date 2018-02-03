pipeline{
  agent any
  stages{

    stage ('python-project'){
      steps{
        sh 'python newfile.py'
      }
    }
    stage('merge development to master'){
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
        sh "git checkout master"
        echo "pull latest from master"
	sh 'git pull'
        echo "merging development into master"
        sh 'git merge development'
        echo "Pushing to remote"
        sh 'git push origin'
      }
    }
    stage('promote to green'){
      when{
        branch 'master'
      }
      steps{
        sh "if ![-d  '/var/www/html/green'];then mkdir /var/www/html/green; fi"
        sh "cp logs/myOutFile.txt /var/www/html/green"
      }
    }
  }
}
