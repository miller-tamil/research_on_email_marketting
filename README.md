# research_on_email_marketing
Hi there..!
This is my final year project work start on June 2015 and will be end around January 2016. so for my first commit i have deposit my early pre-processing works on text mining. and i let it public for review and guide . reviews are appreciated..!

<b><i>Introduction</i></b>
For my subject line study, i try to use a different strategy . There are few researches made on "Creating a effective email subject line " to increasing the open rate.and also there are so effective too. like  <i>[MailChimp](http://kb.mailchimp.com/tag/subject+line)<i> analyzed the open rates for over 200 million emails. Open rates ranged from 93% to 0.5%. but I'm trying to do it in a different point of view .
    
   My goal is to develop a recommended system for <b>Email marketing</b>  perspective. Email marketing is directly marketing a commercial message to a group of people using email. In its broadest sense, every email sent to a potential or current customer could be considered email marketing.
In marketing point of view the content should attract the customers. however considering email marketing the subject line is the first thing that attract a customer.among tens of emails daily we need to make sure a normal user open and read a particular marketing email. it's depending on many areas especially human physiology , localization , sentimental , number of characters, passage sequence and so on. therefore, behalf of analyzing the open rate of normal email data I'm trying to match real world marketing advertisement sequence data and personal email data. 

_<b>data set</b>_

<i>[dataset1-	open-advertising-dataset](https://code.google.com/p/open-advertising-dataset/)</i>
This repository contain more than 5000 advertisement sequence exacted form 15000 website advertisement and clean all the redundancies by using python script. 
Especially this data set contain csv files of Google [ad-words bids details](https://code.google.com/p/open-advertising-dataset/downloads/list) for UK and USA.set 
You can download the data set and open it in csv format . here are some details that files contain.
#key words in csv files :

<b>click-through rate(CRT)</b>

Short for click-through rate, the ratio of the number of times a user clicks on an online advertisement per number of viewers who view the Web site that has the advertisement on it. For example, if one out of 100 people who visit a specific Web site click on an advertisement and are taken to the advertiser's site, then the CTR of that advertisement is 1/100, or 1%.

<b>Cost Per Click(CPC)</b>
Stands for "Cost Per Click," and is used in online advertising. CPC defines how much revenue a publisher receives each time a user clicks an advertisement link on his website. For example, a publisher may place text or image-based ads on his website. When a visitor clicks one of the advertisements, he or she is directed to the advertiser's website. Each click is recorded by the advertiser's tracking system and the publisher is paid a certain amount based on the CPC.

<b>Cost-per-thousand impressions (CPM)</b>
CPM bidding means that you pay based on the number of impressions (times your ads are shown) that you receive on the Google Display Network. Starting this year, CPM bidding will be replaced by viewable CPM bidding. Existing CPM bids will eventually be transitioned to vCPM automatically. Learn more about using viewable CPM bids.

CPM stands for cost-per-thousand impressions, so you pay for each set of a thousand views of your ad. You set CPM bids to tell Google how much you're willing to pay for that set of impressions.
CPM bidding is best suited for advertisers who are focused on brand awareness. For advertisers whose main goal is sales or website traffic, CPC bidding (pay for each click on your ad) might be a better option.
You set a maximum CPM (or "max CPM") bid as the highest amount that you're willing to pay for 1,000 views of your ad.

<b>Understanding ad position and Ad Rank(1 & 0)</b>
Ad position is the order in which your ad shows up on a page. For example, an ad position of "1" means that your ad is the first ad on a page. In general, it's good to have your ad appear higher on a page because it's likely that more customers will see your ad. Ads can appear on the top of a search results page, on the side of the page, or on the bottom of the page.

[dataset2 - enron Email dataset](https://www.cs.cmu.edu/~./enron/) This data set contain 0.6M personal Emails of 150 individual . and i add my very own email collection to it. ;).
here i have extract around 80,000 ignored emails from delete_items and more or less 0.55M Prioritized inbox-mails.

By maping these datasets i'm trying to analys 
1.Statistical Lexical Analysis
2.Sequence Analysis 
3.Sentimental Analysis
4.Psychological Implications.

and by overall conclusion looking forward to come up with a best recomender system .
                                            
                                                                    
                                                                                    to be continue ...
                                                                                    
    Google adword dataset ...                                                                                
Average position (Avg. Pos.)

A statistic that describes how your ad typically ranks against other ads. This rank determines in which order ads appear on the page.

The highest position is "1," and there is no "bottom" position. An average position of 1-8 is generally on the first page of search results, 9-16 is generally on the second page, and so on. Average positions can be between two whole numbers. For example, an average position of "1.7" means that your ad usually appears in positions 1 or 2.
Your ad's rank can change, causing its position on the page to fluctuate as well, so your average position can give you an idea of how often your ad beats other ads for position. However, the most important thing is to find what's profitable for you, which might not be to show in the top position.
Average position may be less useful in optimizing for performance on the Google Display Network because of the diversity of websites on this network. If you want to measure performance on the Display Network, we recommend focusing on metrics such as conversions and ROI.
You can see an "Avg. Pos." column for your ads, campaigns, and other elements, but average position is generally most useful to look at for your keywords. By seeing how your ad typically ranks when it's triggered by one of your keywords, you can try to influence your position by changing the keyword's bid.

Average cost-per-click (Avg. CPC)

The average amount that you've been charged for a click on your ad. Average CPC is calculated by dividing the total cost of your clicks by the total number of clicks.

For example, if your ad receives two clicks, one costing $0.20 and one costing $0.40, your average CPC for those clicks is $0.30.
Average CPC is based on your actual CPCs (the actual amount you're charged for a click on your ad), which might be different than your maximum CPCs (the highest amount that you're willing to pay for a click).
To see your average CPC amounts, look at the "Avg. CPC" column in one of the tables within your Campaigns tab.

Clickthrough rate (CTR)

A ratio showing how often people who see your ad end up clicking it. CTR can be used to gauge how well your keywords and ads are performing.

CTR is the number of clicks that your ad receives divided by the number of times your ad is shown expressed as a percentage (clicks ÷ impressions = CTR).

For example, if you had 5 clicks and 1000 impressions, then your CTR would be 0.5%. Here's how it's calculated:
CTR calculation
Each of your ads and keywords have their own CTRs that you can see listed in your account. Find them on your Campaigns tab
A high CTR is a good indication that users find your ads helpful and relevant. CTR also contributes to your keyword's expected CTR (a component of Quality Score), which can affect your costs and ad position. Note that a good CTR is relative to what you're advertising and on which networks.
You can use CTR to gauge which ads and keywords are successful for you and which need to be improved. The more your keywords and ads relate to each other and to your business, the more likely a user is to click on your ad after searching on your keyword phrase.

Impressions: Definition

How often your ad is shown. An impression is counted each time your ad is shown on a search result page or other site on the Google Network.

Each time your ad appears on Google or the Google Network, it's counted as one impression.
In some cases, only a section of your ad may be shown. For example, in Google Maps, we may show only your business name and location or only your business name and the first line of your ad text.
However, when someone searches using Google Instant, an impression can be counted when one of these occur:
Person begins to type and then clicks anywhere on the page like a search result, ad, or related search
Person types a search and then clicks the "Search" button, presses Enter, or selects a predicted query from the drop-down menu
Person stops typing, and the results are displayed for a minimum of three seconds
You'll sometimes see the abbreviation "Impr" in your account showing the number of impressions for your ad.









