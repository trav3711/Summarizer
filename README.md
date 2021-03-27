# Summarizer

#### flask RestAPI that summarizes blocks of text and returns a five sentence summary

**submit your HTTP requests to:**
`https://my-summarizer.herokuapp.com/rest`

**Example GET request**
```
{
  "text": this could be a big old block of text
  "summary_length": n
}
```

**Example payload**
```
{
  "summary": a summary  of length n of your block of text
}
```
