# AirBnB Clone
Welcome to the AirBnB clone project!     
The AirBnB clone project is a complete web application, integrating database storage, a back-end API, and front-end interfacing in a clone of AirBnB.    
The project currently does not implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.   

# description of the command interpreter(console):

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

# how to start it
- step 1: clone the repository:    
```
$ git clone https://github.com/eric4477/AirBnB_clone.git
```    
- step 2: get into the project by typing:   
```
$ cd AirBnB_clone 
```    
- step 3: run it:   
```
$ ./console.py
```    

# how to use it
- For interactive mode  
```  
 ~/AirBnB_clone$  ./console.py     
(hbnb)help   
   
Documented commands (type help <topic>):    
========================================    
EOF  all  create  destroy  help  quit  show  update    

(hbnb)create User    
3dfa4824-a257-4efd-a652-9c8179296fb8    
(hbnb)
```
- non-interactive mode    
```
~/AirBnB_clone $ echo "help" | ./console.py    
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
~/AirBnB_clone $
~/AirBnB_clone $ cat test_help
help
~/AirBnB_clone $
~/AirBnB_clone $ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
~/AirBnB_clone $
```

# examples   
- Using *create* command to create new user     
```  
 ~/AirBnB_clone$  ./console.py     
(hbnb)help   
   
Documented commands (type help <topic>):    
========================================    
EOF  all  create  destroy  help  quit  show  update    

(hbnb)create User    
3dfa4824-a257-4efd-a652-9c8179296fb8    
(hbnb)
```

## Acknowledgements :pray:

All work contained in this project was completed as part of the curriculum for ALX SE program.

# Authors :black_nib:

**Ahmed Issa** [GitHub](https://github.com/Ahmed-Is3a) | [Twitter](https://twitter.com/ahmedissa0011)  
**Eric** [GitHub](https://github.com/eric4477) | [Twitter](https://twitter.com/eric_george2002)

# License

Public Domain. No copy write protection.
