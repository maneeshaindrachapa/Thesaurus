<h2 align="center">Similar Word Cluster Generator Module</h2>

### Optimized FastText Word Embedding Model

#### Introduction

We didn’t get results as expected by using the Fasttext model which we created by collecting data from Sinhala monolingual corpus available on WMT19 (World Machine Translation 2019). It gave us less synonyms while giving more contextual words. It is because, this text corpus did not contain substantial Sinhala synonyms as we expected. The reason for that was this dataset does not include Sinhala synonym data, because this dataset is crawled from a Sinhala public news websites and social media sites. Therefore, we fed synonyms sets to the Fasttext model.

Data sources like Sinhala textbooks (Ordinary Level) include some number of synonyms, but not considerable number of synonyms for a thesaurus. Therefore, we investigated synonyms rich data sources such as Madhura online dictionary and Concise dictionary.

As the synonym datasets for the system we crawled Sinhala synonym sets from Madhura dictionary by submitting an English dataset to the Madhura application URL and extract the similar meaning word from the response. These synonym sets were not enough to feed the model. So, we used the Concise dictionary to extract furthermore synonym sets.

There are lot of issues in the data. Therefore, we fixed those issues before feeding synonym sets into the Fasttext model. The synonym sets which we crawled from the Madura online dictionary contained related synonyms as well as unrelated words. Therefore, we had to manually look some of those words and fix them. Also, Concise dictionary contained lot of garbage data and Unicode errors. Therefore, we had to write script to clean those data and fix Unicode errors. Generally, a dictionary is providing both synonyms and definitions for the words. Therefore, we had to filter synonyms from the Concise dictionary when extracting the data. All the synonyms and definitions for a particular word is separated by ‘;’ sign. Thus, we split each of these phrases by ‘;’ at first. Then if a corresponding phrase has less than 3 words, we assumed it as a synonym of that word. Otherwise we assumed it as a definition.

#### Literature Review

A web crawler is a program or automated script which browses the World Wide Web in an automated methodological manner. This process is known as we are crawling. People can crawl lot of data from the internet by using crawlers without applying much effort. In modern world, crawling become very straight forward with the help of advanced programming concepts.

When training a Fasttext model under a text corpus, there are a lot of parameters need to be adjusted in order to optimize the model. This procedure will help to find the most appropriate parameters set that provide the best results for a given Fasttext model.

#### Data Preparation & Pre-processing

The synonym sets which we crawled from Madhura dictionary doesn’t need any pre-processing work. But the synonym sets which we extracted from Concise dictionary needed fair amount of data pre-processing work. It is because the conversion of the dictionary pdf file format to word/txt format dictionary had a lot of unwanted data for our model training including numbers, special characters, emojis and etc. Therefore, we had to pre-process andclean data and Unicode errors. As the first thing we had to clean this data set using pre-processing script. Then we trained a Fasttext model using this cleaned dataset. But it did not contain substantial Sinhala synonyms as we expected. The reason for that was this dataset does not include Sinhala synonym data, because this dataset is crawled from a Sinhala public news websites and social media sitesand correct the data sets and then we wrote a python script to clean this dictionary data and extract synonyms sets. But to fix some errors by manually, because there are some unidentifiable errors using scripts. After extracting synonyms sets from Concise dictionary, we feed all of these synonyms setl.

#### Model Training

In this phase we mainly used Fasttext tool as our main model building tool to build the vector model. We used Fasttext model training parameters as given below to train this model.

<table class="MsoNormalTable" border="1" cellspacing="0" cellpadding="0" width="596" style="border-collapse:collapse;mso-table-layout-alt:fixed;border:none;
 mso-border-alt:solid black 1.0pt;mso-yfti-tbllook:1536;mso-padding-alt:5.0pt 5.0pt 5.0pt 5.0pt;
 mso-border-insideh:1.0pt solid black;mso-border-insidev:1.0pt solid black">
 <tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:13.05pt">
  <td width="298" valign="top" style="width:223.5pt;border:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:13.05pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-pagination:none;border:none;mso-padding-alt:31.0pt 31.0pt 31.0pt 31.0pt;
  mso-border-shadow:yes"><b style="mso-bidi-font-weight:normal"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Parameter <o:p></o:p></span></b></p>
  </td>
  <td width="298" valign="top" style="width:223.5pt;border:solid black 1.0pt;
  border-left:none;mso-border-left-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt;
  height:13.05pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-pagination:none;border:none;mso-padding-alt:31.0pt 31.0pt 31.0pt 31.0pt;
  mso-border-shadow:yes"><b style="mso-bidi-font-weight:normal"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Changed Value<o:p></o:p></span></b></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1;height:13.05pt">
  <td width="298" valign="top" style="width:223.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt;
  height:13.05pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-pagination:none;border:none;mso-padding-alt:31.0pt 31.0pt 31.0pt 31.0pt;
  mso-border-shadow:yes"><span class="SpellE"><span lang="EN-GB" style="font-size:
  12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:&quot;Times New Roman&quot;">lr</span></span><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><o:p></o:p></span></p>
  </td>
  <td width="298" valign="top" style="width:223.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:13.05pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-pagination:none;border:none;mso-padding-alt:31.0pt 31.0pt 31.0pt 31.0pt;
  mso-border-shadow:yes"><span lang="EN-GB" style="font-size:12.0pt;font-family:
  &quot;Times New Roman&quot;,serif;mso-fareast-font-family:&quot;Times New Roman&quot;">0.025<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2;height:13.05pt">
  <td width="298" valign="top" style="width:223.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt;
  height:13.05pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-pagination:none;border:none;mso-padding-alt:31.0pt 31.0pt 31.0pt 31.0pt;
  mso-border-shadow:yes"><span lang="EN-GB" style="font-size:12.0pt;font-family:
  &quot;Times New Roman&quot;,serif;mso-fareast-font-family:&quot;Times New Roman&quot;">dim<o:p></o:p></span></p>
  </td>
  <td width="298" valign="top" style="width:223.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:13.05pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-pagination:none;border:none;mso-padding-alt:31.0pt 31.0pt 31.0pt 31.0pt;
  mso-border-shadow:yes"><span lang="EN-GB" style="font-size:12.0pt;font-family:
  &quot;Times New Roman&quot;,serif;mso-fareast-font-family:&quot;Times New Roman&quot;">300<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3;height:13.05pt">
  <td width="298" valign="top" style="width:223.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt;
  height:13.05pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-pagination:none;border:none;mso-padding-alt:31.0pt 31.0pt 31.0pt 31.0pt;
  mso-border-shadow:yes"><span lang="EN-GB" style="font-size:12.0pt;font-family:
  &quot;Times New Roman&quot;,serif;mso-fareast-font-family:&quot;Times New Roman&quot;">epoch<o:p></o:p></span></p>
  </td>
  <td width="298" valign="top" style="width:223.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:13.05pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-pagination:none;border:none;mso-padding-alt:31.0pt 31.0pt 31.0pt 31.0pt;
  mso-border-shadow:yes"><span lang="EN-GB" style="font-size:12.0pt;font-family:
  &quot;Times New Roman&quot;,serif;mso-fareast-font-family:&quot;Times New Roman&quot;">10<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:4;height:13.05pt">
  <td width="298" valign="top" style="width:223.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt;
  height:13.05pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-pagination:none;border:none;mso-padding-alt:31.0pt 31.0pt 31.0pt 31.0pt;
  mso-border-shadow:yes"><span class="SpellE"><span lang="EN-GB" style="font-size:
  12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:&quot;Times New Roman&quot;">minCount</span></span><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><o:p></o:p></span></p>
  </td>
  <td width="298" valign="top" style="width:223.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:13.05pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-pagination:none;border:none;mso-padding-alt:31.0pt 31.0pt 31.0pt 31.0pt;
  mso-border-shadow:yes"><span lang="EN-GB" style="font-size:12.0pt;font-family:
  &quot;Times New Roman&quot;,serif;mso-fareast-font-family:&quot;Times New Roman&quot;">2<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:5;mso-yfti-lastrow:yes;height:13.8pt">
  <td width="298" valign="top" style="width:223.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt;
  height:13.8pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-pagination:none;border:none;mso-padding-alt:31.0pt 31.0pt 31.0pt 31.0pt;
  mso-border-shadow:yes"><span class="SpellE"><span lang="EN-GB" style="font-size:
  12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:&quot;Times New Roman&quot;">minn</span></span><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">, <span class="SpellE">maxn</span><span style="mso-spacerun:yes">&nbsp; </span><o:p></o:p></span></p>
  </td>
  <td width="298" valign="top" style="width:223.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:13.8pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-pagination:none;page-break-after:avoid;border:none;mso-padding-alt:31.0pt 31.0pt 31.0pt 31.0pt;
  mso-border-shadow:yes"><span lang="EN-GB" style="font-size:12.0pt;font-family:
  &quot;Times New Roman&quot;,serif;mso-fareast-font-family:&quot;Times New Roman&quot;">0<o:p></o:p></span></p>
  </td>
 </tr>
</tbody></table>

 Here we only have changed the dataset by adding synonyms sets which we extracted from Madhura and Concise dictionaries to the dataset row by row. Therefore, one row will get one synonym set. The Fasttext will identify words in the same row as synonyms, because here we considered a context window size of 5. Therefore, surrounding words will obtain similar vectors. Then the cosine similarity between those vectors become closer to 1. So, we can find the related synonyms more accurately by feeding synonym sets into the dataset.

After we successfully trained our model, we have identified that model gives many related synonyms words (higher percentage), while providing some contextually similar words (lower percentage).

#### Synonyms Extraction

After successfully trained the Fasttext model, we loaded model inlled Gensim to extract the synonyms. We mainly extract the nearest vectors based on cosine distance-based approach.

After we successfully get the output from the Gensim tool then we have filtered the words based on the similarity measure to get the best synonym set for the input word. As an average value for the similarity threshold we have identified that with in cosine similarity 1 to 0.85 we can get best synonyms for the word. Therefore, we have configured the synset extractor with 0.85 similarity threshold filtering after the Gensim extract the words. This model gave us far more better results than the previous Fasttext model which we built just using the text corpus. That is because now the Fasttext model is rich with synonym sets.

#### Summary & Results

After we successfully built the model, we evaluated the model results with our previous implementations with the synset identification. Then we identified that Fasttext model gives more accurate results than all other implementations. Then we implemented the system with this Fasttext model as the primary synset identification.

With the Fasttext model we successfully retrieved synsets with some level of accuracy and after we fed the synsets for the model for optimization, then model behave more accurate than the previous and show the most similar words for an input word to the system.

<figure>  
<img align=center src="https://github.com/maneeshaindrachapa/Thesaurus/blob/master/WorkInProgress/Docs/images/web_interface_2.png?raw=true" style="width:100%">  
<figcaption align=center>Results for word ‘අම්මා’</figcaption>  
</figure>
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjExMTQyMzI1OCw5Mzk4NTExNDIsLTIwNT
A5MzgyNCwtNDY1MzM4NTU1LDE1Njk2NjAzNTUsNzQ5MzcyMjAs
LTYzNDIyMTg3NywxMTkwNzUyOTMzLDExMjg1Mjc0MiwxMzAwMT
A5MDgwLDIxMDI3NDIzMjNdfQ==
-->