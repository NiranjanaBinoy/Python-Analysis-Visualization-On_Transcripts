# Analysis-Visualization-On_Transcripts Using Python
Statistics for two groups of children's transcripts, for distinguishing between the children with SLI and the typically developed (TD) children.

# Analyser: Building a Class for Data Analysis

The task is about collating the required data for analysis. 

The main task is to produce a number of statistics for the two groups of children transcripts. These statistics are those that might serve as good indicators for distinguishing between the children with SLI and the typically developed (TD) children.

The statistics for each of child transcript that we are interested in are: 
  • Length of the transcript — indicated by the number of statements
  • Size of the vocabulary — indicated by the number of unique words
  • Number of repetition for certain words or phrases — indicated by the CHAT symbol [/] 
  • Number of retracing for certain words or phrases — indicated by the CHAT symbol [//]
  • Number of grammatical errors detected — indicated by the CHAT symbol [* m:+ed]
  • Number of pauses made — indicated by the CHAT symbol (.)
  
Note: Since the length of each child transcript is measured by the number of statements, the end of each statement can be determined based on the following punctuation marks: either a full stop ‘.’, a question mark ‘?’, or an exclamation mark ‘!’.

# Visualizer: Building a Class for Data Visualisation

To visualise the statistics collected as graphs. 

The implementation of this visualiser class should make use of the external Python packages, such as Matplotlib in order to create the suitable graphs for comparing the statistics collected for the two groups of children transcripts

