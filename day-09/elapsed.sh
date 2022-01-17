million=1000000
start_time=$(gdate +%s.%3N)
java CountingTimer $million
end_time=$(gdate +%s.%3N)
elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
echo Elapsed time for 1 million count Java was $elapsed seconds


start_time=$(gdate +%s.%3N)
python counting.py $million
end_time=$(gdate +%s.%3N)
elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
echo Elapsed time for 1 million count Python was $elapsed seconds

