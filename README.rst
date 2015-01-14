===================
WordPress to Zinnia
===================

Wordpress2zinnia is package allowing you to migrate from WordPress to
Zinnia.

Installation
============

* Install the package on your system: ::

  $ pip install wordpress2zinnia

* Register the ``'zinnia_wordpress'`` in your ``INSTALLED_APPS``.

Importing from Wordpress
========================

Once you have the XML file of your export, you simply have to do this. ::

  $ python manage.py wp2zinnia path/to/your/wordpress-export.xml

This command will associate the post's authors to User and
import the tags, categories, post and comments.

For the options execute this. ::

  $ python manage.py help wp2zinnia

http://codex.wordpress.org/Tools_Export_SubPanel

From Zinnia to WordPress
========================

We also provides a command for exporting your Zinnia blog to WordPress in
the case you want to migrate on it.

Simply execute this command: ::

  $ python manage.py zinnia2wp > export.xml

Once you have the XML export, you can import it into your WordPress site.

http://codex.wordpress.org/Importing_Content
