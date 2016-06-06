# community_conventions

In which we examine community conventions by looking at image reposts across different subreddits.

To replicate our analyses:

1) Download the [dataset](https://snap.stanford.edu/data/web-Reddit.html) reported in [H. Lakkaraju, J. J. McAuley, and J. Leskovec (2013), *ICWSM*](http://i.stanford.edu/~julian/pdfs/icwsm13.pdf). 

2) Install Google's [Parsey McParseface](https://github.com/tensorflow/models/tree/master/syntaxnet) English parser

3) Run the parser on a text file containing post titles to get conll output by going to the `models/syntaxnet` directory and running:

```
cat ../../titles.txt | syntaxnet/demo.sh > ../../out.txt
```

4) Tranform the conll output back to a csv, which can be joined with the original data and analyzed in the R markdown document
