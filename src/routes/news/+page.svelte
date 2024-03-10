<script lang="ts">
    import { onMount } from 'svelte';
    let news_json;
    let news_topic: string;
    async function get_news() {
        const response = await fetch(`http://localhost:3000/news/?topic=${encodeURIComponent(news_topic)}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        news_json = await response.json();
    }

    onMount(async () => {
        news_topic = "Top News";
        news_json = await get_news();
    });

</script>
<h2 class=" text-center text-teal-light text-3xl font-mono m-16"> NEWS TOOL!</h2>
<form class="md:flex-col md:justify-center mb-6" on:submit|preventDefault={get_news}>
    <label for="download_path"></label>
    <div class=" flex justify-center">
        <input class="shadow appearance-none border rounded-full m-4 w-2/3 py-2 px-3 bg-background-dark text-text-light leading-tight focus:outline-none focus:shadow-outline" type="text" bind:value={news_topic} placeholder="Enter News Topic" />
        <button type="submit" class=" bg-button-dark text-text-light font-bold px-3 rounded-md inline-flex items-center py-0">
            Get NEWS
        </button>
    </div>
</form>

{#if news_json !== undefined}
    {#each news_json as news}
        <ul class="flex-col">
            <li class="flex-col max-w-8xl rounded overflow-hidden shadow-lg bg-background-dark m-8 p-8 border-teal-light border">
                <a href={news.link} target="_blank" class=" text-text-light text-2xl font-mono m-4">{news.title}</a>
                <p class="m-4 text-teal-light">{@html news.description}</p>
            </li>
        </ul>
    {/each}
{/if}

<style lang="postcss">
    :global(html) {
      background-color: theme(colors.background.dark);
    }
  </style>