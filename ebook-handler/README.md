# E-Book Handler
E-book handler is a simple python program that will move your recently
downloaded ebooks from ```~/Downloads/``` to ```~/bookshelf/```. The program
can also move over all of the books that you have stored locally to your kindle.
This feature is currently only supported for the ```macos``` file-system.

## Defaults
* .pdf store away file size is 15MB
* search path is ```~/Downloads/```
* store path is ```~/library/```

## Commands
* ```./ebookhandler.py -l``` list all of the books on your local bookshelf
* ```./ebookhandler.py -s``` move ebooks from ```~/Downloads/``` to ```~/bookshelf/```
* ```./ebookhandler.py -c``` configure and setup the environment
* ```./ebookhandler.py -ctk``` copy bookshelf to kindle
