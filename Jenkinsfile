pipeline{
  agent any
  stages{

    stage ('python-project'){
      steps{
        sh 'python newfile.py'
	echo "ID"
	sh 'id'
	echo "PWD"
	sh 'pwd'
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
        echo "pull latest from master"
	sh 'git checkout master'
        echo "merging development into master"
	sh 'git merge development'
        echo "Pushing to remote"
	sh 'git push origin master'
      }
    }
    stage('promote to green'){
      when{
        branch 'master'
      }
      steps{
        sh "if ![ -d  '/var/www/html/green']; then mkdir /var/www/html/green; fi"
        sh "if ![-d  '/var/www/html/green'];then mkdir /var/www/html/green; fi"
        sh "cp logs/myOutFile.txt /var/www/html/green"
      }
    }
  }
}
