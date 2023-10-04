# Initial values are specified in the BEGIN block
BEGIN {
   FS = "\t";
   OFS = "_";

}

# Actions for each line of input specified between the {} brackets
{
   count++;
   # Check if the first field from the file isn't a hash symbol
   if ($1 != "#") {
       print "Currently doing " count;
       # Calculate and accumulate values from the third and twelfth fields
       total = total + ($12 * $3);
   }
}

# Commands only done at the END of ALL input between the END{} brackets
END {
   print "The total for " count " lines was " int(total) > "awkoutputfile.txt";
   print "Script run complete." >> "awkoutputfile.txt";
   print "Script run complete.";
   system("ls -alrt *awk*");
}
