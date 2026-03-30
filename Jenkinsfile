pipeline{
  agent any
  stages{
    stage('Update/Install packages in the NetMan VM'){
      steps{
        sh '''
        pip install ncclient
        pip install pandas
        pip install ipaddress
        pip install netaddr
        pip install prettytable
        '''
      }
    }
    stage('Checking and fixing violations'){
      steps{
        sh '''pylint netman_netconf_obj2.py --disable=bad-indentation,f-string-without-interpolation,consider-using-f-string,pointless-string-statement'''
      }
    }
    stage('Running the application'){
      steps{
        sh '''python netman_netconf_obj2.py'''
      }
    }
    stage('Unit Test'){
      steps{
       sh '''python testcases.py'''
      }
    }
    stage('Lint Python') {
    sh '/usr/bin/pylint netman_netconf_obj2.py > pylint.txt'
    recordIssues tools: [pyLint pattern: 'pylint.txt']
    }
  }
  post {
      always {
          emailext(
              subject: "Jenkins Build Completed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
              body: "Jenkins Build Completed. Check details at ${env.BUILD_URL}",
              to: 'kavyamahadev2016@gmail.com',
              from: 'kavyamahadev2016@gmail.com',
              replyTo: 'kavyamahadev2016@gmail.com'
          )
      }
  }
}
