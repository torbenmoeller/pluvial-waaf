# How to use this project
Use this glcoud command to deploy Flask as a Google Cloud Function.
```bash
gcloud functions deploy waaf --runtime python39 --trigger-http --allow-unauthenticated --entry-point gcp_entry_point 
```

You can find more information on my 
[blog post](https://pluvial.dev/post/webserver-as-a-function2/)

# Acknowledgements
The code comes from this 
[Stackoverflow answer](https://stackoverflow.com/questions/53488766/using-flask-routing-in-gcp-function/66026762#66026762) 
that was provided by [Martin](https://stackoverflow.com/users/4443309/martin).

# Contact
Get in touch: [contact@pluvial.dev](contact@pluvial.dev)
