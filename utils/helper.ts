export async function loginAPI(request: any, username: string, password: string) {
  const res = await request.post('/api/login', {
    data: { username, password }
  });

  return await res.json();
}