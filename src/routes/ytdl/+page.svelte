<script lang="ts">
    import { onMount } from 'svelte';
    import { createEventDispatcher } from 'svelte';
    import { page } from '$app/stores';

    let video_filename: string;

    const dispatch = createEventDispatcher();
    let url: string;
    let download_path:string;

    encodeURIComponent

    async function download() {
        const response = await fetch(`http://localhost:3000/ytdl/?video_url=${encodeURIComponent(url)}&download_path=${encodeURIComponent(download_path)}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/html'
            }
        });
        console.log(response);
        return response;
    }
</script>

<h2 class=" text-center text-fuchsia-200 text-4xl underline font-mono m-16"> Welcome to ZEUS's YouTube Downloader!</h2>

<form class="md:flex-col md:justify-center mb-6" on:submit|preventDefault={download}>
    <label for="download_path"></label>
    <input class="shadow appearance-none border rounded m-4 w-1/3 py-2 px-3 text-red-700 leading-tight focus:outline-none focus:shadow-outline" type="text" bind:value={download_path} placeholder="Enter Download Path" />
    
    <div class="flex">
        <label for="url"></label>
        <input class="shadow appearance-none border rounded m-4 w-2/3 py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="text" bind:value={url} placeholder="Enter YouTube URL" />
        <button type="submit" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold px-6 rounded-full inline-flex items-center">
            <svg class="fill-current w-4 h-4 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M13 8V2H7v6H2l8 8 8-8h-5zM0 18h20v2H0v-2z"/></svg>
            Download
        </button>
    </div>
</form>

{#if video_filename}
    <h3>Video Title: {video_filename}</h3>
{/if}

<style lang="postcss">
    :global(html) {
      background-color: theme(colors.slate.800);
    }
  </style>