pipeline{
  agent any
  stages{
    stage('Update/Install packages in the NetMan VM'){
      steps{
        pip install nccclient
        pip install pandas
        pip install ipaddress
        pip install netaddr
        pip install prettytable
      }
    }
    stage('Checking and fixing violations'){
      steps{
        pylint netman_netconf_obj2.py
      }
    }
    stage('Running the application'){
      steps{
        python netman_netconf_obj2.py 
      }
    }
    stage('Unit Test'){
      steps{
        python unit_tests.py 
      }
    }
  }
}
