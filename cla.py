import click
import requests

# the apikey from newsapi.org
API_KEY = '5f81b593f35d42a8980313250c03d7e7​'

@click.group()
def main():
        """
        NewsNow is a news application that offers a list of 4 news sources from which a choice of a preferred source is made,
        from that choice, a list of the top 10 headlines is got,
        The news headline has a title, description and a url in case the user needs to follow up on the news story
        The user also needs to have a valid news api created from http://www.newsapi.org
        """
        pass

@main.command()

def listsources():
	""" Lists 4 sources from the API """
	main_url = " https://newsapi.org/v2/sources?apiKey=5f81b593f35d42a8980313250c03d7e7"

	# fetching data in json format 
	open_source = requests.get(main_url).json() 

	# getting all articles in a string sources
	source = open_source["sources"] 

	# empty list which will 
	# contain all trending newssources 
	results = [] 
	
	for k in source: 
                results.append(k["id"])
            
   	
	for w in results[0:4]:
            print(w)	


@main.command()
def topheadlines():
          """ Please enter your choice from the listsources """
          newsSource = click.prompt("Please enter your choice from listsources")
    
          main_url = "https://newsapi.org/v2/top-headlines?apiKey=f45fa2c71932483f832f0cc745af0325&sources="+newsSource

	# fetching data in json format 
          open_headline = requests.get(main_url).json() 

	# getting all headlines in a string articles 
          headline = open_headline["articles"] 

	# empty list which will 
	# contain all trending newssources 
          output = [] 
	
          for h in headline: 
                click.echo('\n')
                click.secho(click.style('TITLE: ' + h['title'], fg='red'))
                click.secho(click.wrap_text(h['description']))
                click.secho(click.style('DOMAIN: ' + h['url'], fg='blue'))
           
           	
          for i in output[:11]:
                print(i)


if __name__ == '__main__':
	main()