export async function get(uri) {
  let url = 'http://10.125.218.15:9016';
  let response = await fetch(url + uri);
  return await response.json();
}