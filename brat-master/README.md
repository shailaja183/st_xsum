Using BRAT
==========

Setting up BRAT
---------------

Download the following repositories/data;

* git clone https://github.com/shailaja183/st_xsum.git

For now, I did standalone/quickstart installation using the following;

* conda create -n brat python=3.6

* cd ./brat-master

* ./install.sh

* python standalone.py

Check out the documentation at http://brat.nlplab.org/installation.html for installing brat server configuration.

For first-time installation, it would prompt you to provide a username, password and email address (which is mandatory). Note it down as you might be prompted again in the future. 

*  Open http://0.0.0.0:8001 in your browser (works best with Chrome and Safari). 

Loading annotation examples in BRAT
-----------------------------------

* 'Open' dialog-box will load by default

* Go to example-data/xsum/<directory_you_are_assigned_to_annotate>

Double click to go inside a selected directory\
Double click ../ to move one level back in the directory hierarchy

* Select the first file in your desired directory, Press 'OK'

Navigating in BRAT
------------------

* You can pause/resume your annotation anytime. It would be easier to open an example if you note down the id.

* At any point in time, if you think you need to edit your response, hover over the top bar showing the file name i.e. example-data/xsum/<directory_you_are_assigned_to_annotate>, it will pull up a menu. Then press 'Collection' and choose the file you want to edit. 
There is also a 'Search' (by keyword) button if you do not remember the id of the example you want to edit. 

* If you want to change the reasoning type, simply double-click the incorrect reasoning category over the phrase and change the type. 

* If you want to change the reasoning span, double-click the current reasoning category assigned to the span, then select 'Move'. Then reselect the correct span. 

* This interface is sensitive to spaces so please avoid selecting unnecessary spaces before or after the phrase. 

* If you are not confident of a reasoning category, feel free to add 'Note' while you assign a reasoning type. 

Keyboard Shortcuts
-------------------

The following keyboard shortcuts are accessible in normal visualization or annotation state.\
(When a menu is open, these keyboard shortcuts are disabled.) Note: On Mac, use Cmd instead of Ctrl.

* ESC: clear any open menus (canceling possible modifications) and on-screen messages\
* TAB: open the collection browser\
* CTRL-F: search\
* CTRL-G: next search result (after search)\
* CTRL-H: repeat the previous annotation action on the current search result (after search)\
* Left arrow: previous document (or search result)\
* Right arrow: next document (or search result)

Example Walk-through
--------------------

File starting with ID 00000000 is annotated for demonstration purposes. Following is the explanation of how reasoning categories are assigned. 

ex. 00000000_berts2s  
Does not contain the summary, so no annotation is required. Simply skip and move to the next example. 

ex. 00000000_gold\
Contains the summary. So read the article and the summary.\
Observe hallucination span 'ten sentences' in the summary.\
Now try to break down the hallucination span into small phrases and assign reasoning categories to each. 

In this case,

* ten - any person or model with commonsense knowledge would be able to conclude that the count of sentences in the article is 'ten' though it is not provided anywhere in the article. Counting ability can be considered under 'numerical reasoning' as per the definition below.

* sentences - this phrase is a direct variation of the word 'sentence' which is present in the article. So this is not considered reasoning and we will not assign any category to this phrase. (tl;dr - copying is not reasoning)


Annotation Guidelines
---------------------

More generally, 

* Check if the summary exists. If not, simply go to the next instance
(using the right arrow on the keyboard or right arrow on the top-left corner)

* Carefully read the article and summary

* Carefully observe hallucination spans (with black heading 'Hallucination') in the summary

* Assign Reasoning categories to various phrases WITHIN the hallucination spans by double clicking the phrase. Choose the reasoning category based on the following definition. It will automatically save your responses to the corresponding .ann file. 

* If you think a portion of the hallucination span cannot be concluded from the article or is incorrect, do not assign a reasoning category to it. 

* It is possible that one summary can have multiple hallucination spans and each hallucination span can have multiple reasoning categories for sub-phrases. 

Reasoning categories definition and examples
--------------------------------------------

1. Adjective - "Adjective or Adverb" (inferred about a person or an event in the article) is the key component of the hallucination span\
* Body of a man found -> \<Adjective\> Dead \</Adjective\> man
* Fire broke out -> \<Adjective\> Severely \</Adjective\> burnt

2. CommonNoun - "Common Noun" (inferred about a person or an event in the article) is the key component of the hallucination span - often includes gender pronoun, citizenship, nationality, titles (sir, professor, captain etc.)
* 2 year-old boy, James -> \<CommonNoun\> Toddler \</CommonNoun\> James
* Alex Ferguson -> \<CommonNoun\> Coach \</CommonNoun\> Ferguson
* Comedian -> \<CommonNoun\> French \</CommonNoun\> comedian

(3) ProperNoun - "Proper Noun" (inferred about a person or an event in the article) is the key component of the hallucination span - often includes first name, last name
* Obama -> \<ProperNoun\> Barack \</ProperNoun\> Obama
* Leonardo -> Leonardo \<ProperNoun\> DiCaprio \</ProperNoun\>

(4) Professional - Inference about person's occupation, organization, community or professional associations, work-related taxonomies
* Barack Obama -> \<Professional\> Senator \</Professional\> Obama
* US President -> Works in \<Professional\> White House \</Professional\>
* Trump -> Is a \<Professional\> Republican representative \</Professional\>
* Clothing -> Is a type of \<Professional\> Textile \</Professional\>

(5) Causal - "Verb" (inferred about a person or an event in the article, that is not present in the article) is the key component of the hallucination span
* Activity A banned -> \<Causal\> Illegal \</Causal\> to do A
* Earthquake strikes -> \<Causal\> Forced \</Causal\> people to come out

(6) Numeric - Inference related to quantity/amount/calculation about a particular item based on the article - includes alternative forms such as \% or fractions. Close estimates are also considered
* Person A, B, C -> \<Numeric\> 3 \</Numeric\> people
* quarter -> \<Numeric\> ~26% \</Numeric\>
* 100 to 120 price change -> \<Numeric\> 20% increase \</Numeric\> 

(7) Temporal - Date/month/year/time elapsed/relative time/duration/season related keywords or inference based on the article (but not directly provided)
* War in 1987-1990 -> \<Temporal\> 3 \</Temporal\> years of war
* 1984 -> \<Temporal\> Mid-1980s \</Temporal\>
* Retire next month -> \<Temporal\> Last \</Temporal\> working month

(8) Geographical - Inference related to the geographical relationship between places - includes relative or approximate location using directions east/west/north/south 
* Asia -> Is a \<Geographical\> Continent \</Geographical\>  
* Michigan -> Is a \<Geographical\> State in US \</Geographical\> 
* NY -> Is in \<Geographical\> eastern part of US \</Geographical\> 

(9) ExpertKnowledge - Specific information about an entity or an event that is not expected to be common knowledge and less likely to find a similar instance across the dataset- ex. person's birthday/age, event specifics, company’s  turnover/profits.
* Roger Moore -> is a former \<ExpertKnowledge\> James Bond star \<\ExpertKnowledge\>
* Nicholas winton -> \<ExpertKnowledge\> died aged 106 \<\ExpertKnowledge\>
* IBM -> Had \<ExpertKnowledge\> profits of \$125M in 2010 \<\ExpertKnowledge\>
*  Fiji -> Has \<ExpertKnowledge\> 800 islands \<\ExpertKnowledge\>
*  2020 Olympics -> Was \<ExpertKnowledge\> held in Tokyo \<\ExpertKnowledge\>

(10) Other - There is still some reasoning going on (which requires implicit inference based on the article) but does not fit into any of the above categories/descriptions. Try to explain why you think a phrase belongs to 'other' category by adding a 'Note' while you assign a reasoning type. 
