        const filter = document.getElementById("Filter")
        const number = document.getElementById('number')
        const currentDate = new Date();

        pageList = [{'product':'personal_loan','URL':'/personal-loan'},
                    {'product':'home_loan','URL':'/home-loan'}]

        const Data = []

        function getPageSourceData(page){
            fetch("http://127.0.0.1:8000/real-time-api-page",{
              method: 'POST',
              headers: {
                'Content-Type': 'application/json'
                // Add any other headers your API requires
              },
              body: JSON.stringify({'page':'/personal-loan'})
            })
              .then(response => response.json())
              .then(responseData => {
                return responseData // Output: The API response data
              })
              .catch(error => {
                console.error('Error:', error);
              });
            return apiResponse['source_medium']
        };

        async function GetAllData(requestData) {
          const requestOptions = {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(req uestData)
          };

          try {
            const response = await fetch(url, requestOptions);
            const responseData = await response.json();
            return responseData;
          } catch (error) {
            console.error('Error:', error);
            throw error; // Rethrow the error to be handled by the caller
          }
        }
        pageList.forEach(value => {
            const pageDiv = document.createElement('div');
            pageDiv.id = 'pageDiv';

            const pageScore = document.createElement('p');
            pageScore.id = 'pagePara';
            pageScore.textContent = value;

            pageDiv.appendChild(pageScore)

            number.appendChild(pageDiv)

        })

        function updateFilters(data){
              const sources = new Set();
              const mediums = new Set();
              const campaigns = new Set();

              data.forEach(x=>{
                sources.add(x["data"]["source_medium"].map(row => row[0]))
                mediums.add(x["data"]["source_medium"].map(row => row[1]))
                campaigns.add(x["data"]["source_medium"].map(row => row[2]))
              });

              populateOptions(sourceFilter, sources);
              populateOptions(mediumFilter, mediums);
              populateOptions(campaignFilter, campaigns);

        };


        function populateOptions(selectElement, values) {
          // Clear existing options
          selectElement.innerHTML = '';

          // Add 'All' option as the default
          const allOption = document.createElement('option');
          allOption.value = '';
          allOption.textContent = 'All';
          selectElement.appendChild(allOption);

          // Add options based on values
          values.forEach(value => {
            const option = document.createElement('option');
            option.value = value;
            option.textContent = value;
            selectElement.appendChild(option);
          });
        }

        function updateNumbers(data){
            document.querySelectorAll('#number #pageDiv #pagePara').forEach(value =>{

                value.textContent = new Date().getSeconds();

            })

        }


        updateNumbers();

        setInterval(updateNumbers, 30000);

        console.log('it worked')