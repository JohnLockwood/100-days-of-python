million=1000000
start_time=$(gdate +%s.%3N)
java CountingTimer $million
end_time=$(gdate +%s.%3N)
elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
echo Elapsed time for 1 million count Java was $elapsed ms


start_time=$(gdate +%s.%3N)
python counting_timeit.py $million
end_time=$(gdate +%s.%3N)
elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
echo Elapsed time for 1 million count Python was $elapsed ms

