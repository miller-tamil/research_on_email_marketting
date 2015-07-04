# research_on_email_marketting
Hi there..!
This is my final year project work start on June 2015 and will be end around January 2016. so for my first commit i have deposit my early pre-processing works on text mining. and i let it public for review and guide . reviews are appreciated..!

<b><i>Inroduction</i></b>
For my subject line study, i try to use a different strategy . There are few researches made on "Creating a effective email subject line " to increasing the open rate.and also there are so effective too. like  <i>[MailChimp](http://kb.mailchimp.com/tag/subject+line)<i> analyzed the open rates for over 200 million emails. Open rates ranged from 93% to 0.5%. but I'm trying to do it in a different point of view .
    
   My goal is to develop a recommended system for <b>Email marketing</b>  perspective. Email marketing is directly marketing a commercial message to a group of people using email. In its broadest sense, every email sent to a potential or current customer could be considered email marketing.
In marketing point of view the content should attract the customers. however considering email marketing the subject line is the first thing that attract a customer.among tens of emails daily we need to make sure a normal user open and read a particular marketing email. it's depending on many areas especially human physiology , localization , sentimental , number of characters, passage sequence and so on. therefore, behalf of analysing the open rate of normal email data i'm trying to match real world marketing advetisments sequnce data and personal email data. 

_<b>dataset</b>_

<i>[dataset1-	open-advertising-dataset](https://code.google.com/p/open-advertising-dataset/)</i>
This repositery contain more than 5000 advertisment sequnce extacted form 15000 website advertistments and clean all the redundenncies by using python script. 
Especially this data set contain csv files of google [adwords bids deails](https://code.google.com/p/open-advertising-dataset/downloads/list) for UK and USA.set 
youcan download the data set and open it in csv formart . here are some details that files contain.
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

#[dataset2 - enron Email dataset](https://www.cs.cmu.edu/~./enron/)
This dataset contain 0.6M personal Emails of 150 induviduals . and i add my very own email collection to it. ;).
here i have extract around 80,000 ignored emails from delete_items and more or less 0.55M Preoritized inbox-mail.


