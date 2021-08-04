#!/bin/bash

##Queries the US Census's 5-year American Community survey API for info.  Replace query array with desired variables, and add the appropriate q_human translations at the bottom.  You will need to apply for a (free) US Census API key and replace the key below with yours  List of census tracts -https://www.ffiec.gov/census/  Variables vile - https://api.census.gov/data/2018/acs/acs5/variables.html

#usage: note- no file extension on the dataset OR tracts input file argument = ./washington-state-census-tract.sh data-example tracts-input-file

#backup old files
mkdir -p archive
files="data/census-tract-data-$1-$2.txt"

#archive old version of file (comment out to just append to existing)
#for f in $files
#do
#mv $f archive/$f
#done

#create header column (comment out if not the first run)
#echo "COUNTY|TRACT_NUM|DATA|CENSUS_QUERY|HUMAN_READABLE|DATASET|YEAR" >> washington-state-$1.txt

while read line;
do

location=$(echo $line)

while read line;
do

q=$(echo $line | grep -ioP "^......\_....(?=\,)")
q_human_test=$(echo $line | grep -ioP "(?<=^......\_....\,).*")

#set dataset & year range
dataset="acs5"
for y in {2015..2019} #loop over year range  #REAL VERSION
do

url="https://api.census.gov/data/$y/acs/$dataset?get=NAME,$q&for=tract:$location&key=3f9b852cbbc80fd057c367742e3b2b92244bb964" #insert the query and congressional district strings into the API call

#TESTER
#url="https://api.census.gov/data/2018/acs/acs5?get=NAME,B01001_001E&for=tract:201101&in=state:53%20county:007&key=3f9b852cbbc80fd057c367742e3b2b92244bb964"
page=$(curl -sL "$url" ) #curl the census API

data=$(echo $page | grep -ioP "(?s)(?<=[a-z]\"\,\")\d.*?(?=\"\,\"\d\d\"\,\"\d\d)") #extract just the query result from json package (after the state name, before the state FIPS and district FIPS)

######BEGIN HUMAN-READABLE LABEL SECTION - copy this pattern for whatever variables and locations that apply to your project#####
#translate states and districts into English
tract_num=$(echo $location | grep -ioP "^\d\d\d\d\d\d(?=\&in\=state)") #pull tract number

if [[ "$location" =~ 001$ ]];
then
  county_name="Adams"
fi
if [[ "$location" =~ 003$ ]];
then
  county_name="Asotin"
fi
if [[ "$location" =~ 005$ ]];
then
  county_name="Benton"
fi
if [[ "$location" =~ 007$ ]];
then
  county_name="Chelan"
fi
if [[ "$location" =~ 009$ ]];
then
  county_name="Clallam"
fi
if [[ "$location" =~ 011$ ]];
then
  county_name="Clark"
fi
if [[ "$location" =~ 013$ ]];
then
  county_name="Columbia"
fi
if [[ "$location" =~ 015$ ]];
then
  county_name="Cowlitz"
fi
if [[ "$location" =~ 017$ ]];
then
  county_name="Douglas"
fi
if [[ "$location" =~ 019$ ]];
then
  county_name="Ferry"
fi
if [[ "$location" =~ 021$ ]];
then
  county_name="Franklin"
fi
if [[ "$location" =~ 023$ ]];
then
  county_name="Garfield"
fi
if [[ "$location" =~ 025$ ]];
then
  county_name="Grant"
fi
if [[ "$location" =~ 027$ ]];
then
  county_name="Grays Harbor"
fi
if [[ "$location" =~ 029$ ]];
then
  county_name="Island"
fi
if [[ "$location" =~ 031$ ]];
then
  county_name="Jefferson"
fi
if [[ "$location" =~ 033$ ]];
then
  county_name="King"
fi
if [[ "$location" =~ 035$ ]];
then
  county_name="Kitsap"
fi
if [[ "$location" =~ 037$ ]];
then
  county_name="Kittitas"
fi
if [[ "$location" =~ 039$ ]];
then
  county_name="Klickitat"
fi
if [[ "$location" =~ 041$ ]];
then
  county_name="Lewis"
fi
if [[ "$location" =~ 043$ ]];
then
  county_name="Lincoln"
fi
if [[ "$location" =~ 045$ ]];
then
  county_name="Mason"
fi
if [[ "$location" =~ 047$ ]];
then
  county_name="Okanogan"
fi
if [[ "$location" =~ 049$ ]];
then
  county_name="Pacific"
fi
if [[ "$location" =~ 051$ ]];
then
  county_name="Pend Oreille"
fi
if [[ "$location" =~ 053$ ]];
then
  county_name="Pierce"
fi
if [[ "$location" =~ 055$ ]];
then
  county_name="San Juan"
fi
if [[ "$location" =~ 057$ ]];
then
  county_name="Skagit"
fi
if [[ "$location" =~ 059$ ]];
then
  county_name="Skamania"
fi
if [[ "$location" =~ 061$ ]];
then
  county_name="Snohomish"
fi
if [[ "$location" =~ 063$ ]];
then
  county_name="Spokane"
fi
if [[ "$location" =~ 065$ ]];
then
  county_name="Stevens"
fi
if [[ "$location" =~ 067$ ]];
then
  county_name="Thurston"
fi
if [[ "$location" =~ 069$ ]];
then
  county_name="Wahkiakum"
fi
if [[ "$location" =~ 071$ ]];
then
  county_name="Walla Walla"
fi
if [[ "$location" =~ 073$ ]];
then
  county_name="Whatcom"
fi
if [[ "$location" =~ 075$ ]];
then
  county_name="Whitman"
fi
if [[ "$location" =~ 077$ ]];
then
  county_name="Yakima"
fi

echo "$county_name | $tract_num | $data | $q | $y" #output to sdout
echo "$county_name|$tract_num|$data|$q|$q_human_test|$dataset|$y" >> data/census-tract-data-$1-$2.txt #output to pipe-separated text file.

done
done<$1.csv
done<$2.txt
