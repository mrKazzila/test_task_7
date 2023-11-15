<h1 align="center">
  Simple doc
</h1>

<hr>

<p align="center">
   <a href="#documentation">Documentation</a>
</p>


## Documentation
<details>
<summary><strong>API Documentation</strong></summary>

**`POST` | Create short url: [`http://localhost:8000/get_form`](http://localhost:8000/get_form)**

Example:
   - Request
      ```
      [
        {
          "field": "string",
          "value": "+7 123 456 90 12"
        }
      ]
      ```
   - Response (if form template found)

      ```
        {
          "template_name": "Form template name"
        }
      ```
   - Response (if form template not found)

      ```
        {
         "field": "text",
         "value": "phone"
        }
      ```

</details>
