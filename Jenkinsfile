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
    stage('Lint') {
        steps {
            // Run pylint and save output
            sh "pylint --output-format=parseable netman_netconf_obj2.py > pylint.log || :"

            // Record pylint warnings with thresholds
            recordIssues(
                tools: [pyLint(pattern: 'pylint.log')],
                healthy: 5,      // 100% health if ≤ 5 warnings
                unhealthy: 10,   // 0% health if ≥ 10 warnings
                thresholdLimit: 10,   // fail build if >10 warnings
                qualityGates: [
                    [$class: 'QualityGate', threshold: 10, unstable: true]
                ]
            )
        }
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
