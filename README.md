
<h1>Introduction</h1> 

The app works dynamically and returns Github issues of specific repositories through specific labels.
Repositories, labels and programming languages are expected to saved to database.

```e.g. search page ```  

![Image](/projectapp/static/images/search_page.png?raw=true "search page")

```e.g. result page ``` 


![Image](/projectapp/static/images/result_page.png?raw=true "result page")

## Installation

Clone the repository to your local machine:

```
git clone https://github.com/zeyytas/githubAPI-project.git
```

Recommended to use `virtualenv` for development:

- Start by installing `virtualenv` if you don't have it
```
pip install virtualenv
```

- Create a virtual environment
```
virtualenv env
```

- Enable the virtual environment
```
source env/bin/activate
```

- Install the python dependencies on the virtual environment
```
pip install -r requirements.txt
```

## Action
<small>
   
GET         /api </small>

## Attributes

<small>
   
   - language

   ```e.g.   /language```


   - label

   ```e.g.   /label```
   
   
   - repository
   'l' parameter refers language
   
   ```e.g.   /repository?l=Python```
   
</small>
