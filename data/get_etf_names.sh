
ETFS=`cat ./etf_names.txt`
for ETF in $ETFS
do
    rm ./etfs/$ETF.csv
    touch ./etfs/$ETF.csv
    curl -o ./etfs/$ETF.csv\
        https://query1.finance.yahoo.com/v7/finance/download/$ETF?period1=628387200&period2=1553900400&interval=1d&events=history&crumb=U73b6yX9lv4
done
