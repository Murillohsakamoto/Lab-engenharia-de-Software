   pipeline {
       agent any
       triggers { githubPush() }
       stages {
           stage('Preparar ambiente') {
               steps {
                   sh '''
                       python3 -m venv venv
                       . venv/bin/activate
                       pip install -r requirements.txt
                   '''
               }
           }
           stage('Testes') {
               steps {
                   sh '''
                       . venv/bin/activate
                       python -m pytest --junitxml=resultados.xml
                   '''
               }
           }
       }
       post { always { junit 'resultados.xml' } }
   }
