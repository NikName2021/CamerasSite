
const app = Vue.createApp({
    el: '#app',
    mounted() {
        this.getArtists()
    },
    data(){
        return {
            artists: []

        }
    },
    methods: {
        getArtists() {
            axios.get('api/network')
                .then(res => {
                    this.artists = res.data
                    console.log(res.data)
                })
                .catch(e => {
                    console.log(e)
                })

        },
    }
});
app.mount('#app')