.. code::

   # clone
   git clone https://github.com/datakurre/plone-pip
   cd plone-pip

   # create and update Python 2.7 venv
   virtualenv env
   env/bin/pip install -U pip setuptools

   # install buildout.requirements generated requirements and extras
   env/bin/pip install -r requirements-5.1rc2.txt -r requirements.txt

   # init ZODB with admin:admin user
   env/bin/plonecli instance -C zope.conf run admin.py

   # serve Plone
   env/bin/plonecli instance -C zope.conf fg

   # installing existing add-on
   env/bin/pip install collective.easyform
   env/bin/pip install plone.app.imagecropping

   # developing a new add-on
   source env/bin/activate
   plonecli create addon my.addon
   cd my.addon
   python setup.py develop
