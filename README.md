# PyGeekle'22 Python Summit

This project was for a presentation at the conference around the use of s3 buckets with Analytics and Data Science. Pandas doesnt have the best connection methods to s3, so i walk through a simple importer and exporter code block for Pandas and s3 as well as spoke of the idea of a 'Smart s3 bucket' where common data tasks can be automated if you have any manual intensive or high frequency processes, using Pandas and Boto3.

## Screenshot

![alt text](./readme_images/pygeekle_screenshot.png "Title")

## Presentation
<div style="position: relative; width: 100%; height: 0; padding-top: 56.2500%;
 padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
 border-radius: 8px; will-change: transform;">
  <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
    src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAFLayUgobs&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
  </iframe>
</div>
<a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAFLayUgobs&#x2F;view?utm_content=DAFLayUgobs&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Using s3</a> by Brad Webb 

## AWS s3 get csv code
    ```
    response = s3.get_object(Bucket=input_bucket, Key=file_key)
    new_file = pd.read_csv(response['Body'])
    ```

## AWS s3 put csv code

    ```
    with StringIO() as csv_buffer:
        output_df.to_csv(csv_buffer, index=False)
        response = s3.put_object(
            Bucket=output_bucket, Key=output_key, Body=csv_buffer.getvalue()
        )
    ```
## Smart s3 Bucket

I covered off the idea of a 'Smart s3 bucket' with Pandas, where you can upload files to and have lambda functions trggered to 'Process' data files for you. Also can reduce manual work and tediuos tasks, that are all too common in Analytics and Data Science.

## AWS instructions

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation




  



