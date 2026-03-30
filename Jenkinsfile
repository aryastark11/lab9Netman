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
        sh '''python netman_netconf_obj2.py '''
      }
    }
    stage('Unit Test'){
      steps{
       sh '''python testcases.py'''
      }
    }
  }
}
