Using BRAT
==========

Setting up BRAT
---------------

Download following repositories/data;

(1) git clone https://github.com/shailaja183/st_xsum.git

For now, I did standalone/quickstart installation using following;

(2) conda create -n brat python=3.6
(3) cd ./brat-master/
(4) ./install.sh
(5) python standalone.py

Check out documentation at http://brat.nlplab.org/installation.html for installing brat server configuration.

For first time installation, it would prompt you to provide username, password and email address (which is mandatory). Note it down as you might be prompted again in future. 

(6) Open http://0.0.0.0:8001 in your browser (works best with Chrome and Safari). 

Loading annotation examples in BRAT
-----------------------------------

(1) Open menu will load by-default.

(2) Go to examples/xsum/<directory_you_are_assigned_to_annotate>

Double click to go inside a selected directory
Double click ../ to move one level back in directory hierarchy

(3) Select the first file in your desired directory, Press 'OK'

Navigating in BRAT
------------------

(1) You can pause/resume your annotation anytime. It would be easier to open example if you note down the id.

(2) At any point in time, if you think you need to edit your response, hover over top bar showing file name i.e. examples/xsum/<directory_you_are_assigned_to_annotate>, it will pull up a menu. Then press 'Collection' and choose file you want to edit. 
There is also 'Search' (by keyword) button if you do not remember the id of the example you want to edit. 

(3) If you want to change the reasoning type, simply double click the incorrect reasoning category over the phrase and change the type. 

(4) If you want to change the reasoning span, double click the current reasoning category assigned to the span, then select 'Move'. Then reselect the correct span. 

(5) This interface is sensitive to spaces so please avoid selecting unnecessary spaces before or after the phrase. 

(6) If you are not confident of a reasoning category, feel free to add 'Note' while you assign reasoning type. 

Key-board Shortcuts
-------------------

The following keyboard shortcuts are accessible in normal visualization or annotation state. (When a menu is open, these keyboard shortcuts are disabled.) Note: On Mac, use Cmd instead of Ctrl.

ESC: clear any open menus (canceling possible modifications) and on-screen messages
TAB: open the collection browser

CTRL-F: search
CTRL-G: next search result (after search)
CTRL-H: repeat the previous annotation action on the current search result (after search)
Left arrow: previous document (or search result)
Right arrow: next document (or search result)

Example Walk-through
--------------------

File starting with ID 00000000 is annotated for demonstration purpose. Following is the explanation about how reasoning categories are assigned. 

ex. 00000000_berts2s  
Does not contain the summary, so no annotation is required. Simply skip and move to next example. 

ex. 00000000_gold
Contains the summary. So read the article and the summary.
Observe hallucination span 'ten sentences in total' in the summary.
Now try to break-down hallucination span into small phrases and assign reasoning categories to each. 

In this case,

(i) ten - any person or model with commonsense knowledge would be able to conlude that the count of number of sentences in article is 'ten' though it is not provided anywhere in the article. Counting ability can be considered under 'numerical reasoning' as per definition below.

(ii) sentences - this phrase is a direct variation of the word 'sentence' which is present in the article. So this is not considered as reasoning and we will not assign any category to this phrase. (tl;dr - copying is not reasoning)


Annotation Guidelines
---------------------

More generally, 

(1) Check if Summary exists. If not, simply go to next instance
(using the right arrow on the keyboard or right arrow on top-left corner)

(2) Carefully read the article and summary

(3) Carefully observe hallucination spans (with black headings Hallucination) in the summary

(4) Assign Reasoning categories to various phrases WITHIN the hallucination spans by double clicking the phrase.

Choose the reasoning category based on the following definition. 
It will automatically save your responses to corresponding .ann file. 

(5) If you think a portion of the hallucination span cannot be concluded from the article or is incorrect, do not assign a reasoning category to it. 

(6) It is possible that one summary can have multiple hallucination span and each hallucination span can have multiple reasoning categories for sub-phrases. 

Reasoning categories definition and examples
--------------------------------------------

(i) Adjective - "Adjective or Adverb" (inferred about a person or an event in the article) is the key component of the hallucination span
ex. 
Body of a man found -> <Ajdective> Dead </Ajdective> man
Fire broke out -> <Ajdective> Severely <Ajdective> burnt

(ii) CommonNoun - "Common Noun" (inferred about a person or an event in the article) is the key component of the hallucination span - often includes gender pronoun, citizenship, nationality, titles (sir, professor, captain etc.)
ex. 
2 year-old boy, James -> <CommonNoun> Toddler </CommonNoun> James
Alex Ferguson -> <CommonNoun> Coach </CommonNoun> Ferguson
Comedian -> <CommonNoun> French </CommonNoun> comedian

(iii) ProperNoun - "Proper Noun" (inferred about a person or an event in the article) is the key component of the hallucination span - often includes first name, last name. 
ex.
Obama -> <ProperNoun> Barack </ProperNoun> Obama
Leonardo -> Leonardo <ProperNoun> DiCaprio </ProperNoun> 

(iv) Professional - Inference about person's occupation, organization, community or professional associations, work related taxonomies
ex. 
Barack Obama -> <Professional> Senator </Professional> Obama 
US President -> Works in <Professional> White House </Professional> 
Trump -> Is a <Professional> Republican representative </Professional>
Clothing -> Is a type of <Professional> Textile </Professional>

(v) Causal - "Verb" (inferred about a person or an event in the article, that is not present in the article) is the key component of the hallucination span
ex.
Activity A banned -> <Causal> Illegal </Causal> to do A 
Earthquake strikes -> <Causal> Forced </Causal> people to come out

(vi) Numeric - Inference related to quantity/amount/calculation about a particular item based on the article - includes alternative forms such as \% or fractions. Close estimates are also considered.
ex. 
Person A, B, C -> <Numeric> 3 </Numeric> people 
quarter -> <Numeric> ~26% </Numeric>  
100 to 120 price change -> <Numeric> 20% increase </Numeric> 

(vii) Temporal - Date/month/year/time elapsed/relative time/duration/season related keywords or inference based on the article (but not directly provided)
ex.
War in 1987-1990 -> <Temporal> 3 </Temporal> years of war 
1984 -> <Temporal> Mid-1980s </Temporal> 
Retire next month -> <Temporal> Last </Temporal> working month

(viii) Geographical - Inference related to geographical relationship between places - includes relative or approximate location using directions east/west/north/south
ex. 
Asia -> Is a <Geographical> Continent </Geographical>  
Michigan -> Is a <Geographical> State in US </Geographical>  
NY -> Is in <Geographical> eastern part of US </Geographical> 

(ix) ExpertKnowledge - Specific information about an entity or an event which is not expected to be a common knowledge and less likely to find a similar instance across the dataset- ex. person's birthday/age, event specifics, company’s  turnover/profits.
ex.
Roger Moore -> is a former <ExpertKnowledge> James Bond star <\ExpertKnowledge>
Nicholas winton -> <ExpertKnowledge> died aged 106 <\ExpertKnowledge> 
IBM -> Had <ExpertKnowledge> profits of \$125M in 2010 <\ExpertKnowledge>
 Fiji -> Has <ExpertKnowledge> 800 islands <\ExpertKnowledge> 
 2020 Olympics -> Was <ExpertKnowledge> held in Tokyo <\ExpertKnowledge>

(x) Other - There is still some reasoning going on (which requires implicit inference based on the article) but does not fit into any of the above categories/description. Try to explain why do you think a phrase belongs to other category by adding a 'Note' while you assign reasoning type. 