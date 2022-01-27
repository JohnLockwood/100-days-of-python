start_time=$(gdate +%s.%3N)
./counting
end_time=$(gdate +%s.%3N)
elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
echo Elapsed time for 10 million count in C was $elapsed seconds



