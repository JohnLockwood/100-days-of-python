ten_million=100000000
start_time=$(gdate +%s.%3N)
java CountingTimer $ten_million
end_time=$(gdate +%s.%3N)
elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
echo Elapsed time for 10 million count Java was $elapsed seconds


start_time=$(gdate +%s.%3N)
python counting.py $ten_million
end_time=$(gdate +%s.%3N)
elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
echo Elapsed time for 10 million count Python was $elapsed seconds

