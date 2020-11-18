# Summarizer

#### restful flask API that summarizes blocks of text and returns a five sentence summary

**submit your requests to:**
`https://my-summarizer.herokuapp.com/webhook`

**Example POST**
```
{
  'text': this could be a big old block of text
  'summary_length': n
}
```

**Example GET**
```
{
  'summary': a summary  of length n of your block of text 
}
```
