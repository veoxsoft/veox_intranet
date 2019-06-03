var app = new Vue({
    delimiters: ['((', '))'],
    el: '#app-buzon',
    data: {
        buzon: {}
    },
    methods: {
        resetBuzon: function (){
            this.buzon = {};
        },
        cancel: function (e) {
            e.preventDefault();
            this.resetBuzon();
        }, 
        create: function (e) {
            e.preventDefault();
            this.$validator.validate().then(valid => {
                if (valid) {
                    axios({
                        method: 'POST',
                        url: 'http//google',
                        data: this.buzon
                    }).then(function (response) {
                        console.log(response);
                    }).catch(function (error) {
                        toastr.error(error, 'Ha ocurrido un error!');
                    });
                }
            });
        }
    }
});
