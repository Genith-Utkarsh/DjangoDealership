import React, { useState } from "react";

export default function Register() {
  const [form, setForm] = useState({ username: "", first_name: "", last_name: "", email: "", password: "" });
  const update = (event) => setForm({ ...form, [event.target.name]: event.target.value });
  return (
    <form className="register-form">
      <h1>Sign up</h1>
      <input name="username" placeholder="Username" value={form.username} onChange={update} />
      <input name="first_name" placeholder="First Name" value={form.first_name} onChange={update} />
      <input name="last_name" placeholder="Last Name" value={form.last_name} onChange={update} />
      <input name="email" type="email" placeholder="Email" value={form.email} onChange={update} />
      <input name="password" type="password" placeholder="Password" value={form.password} onChange={update} />
      <button type="submit">Register</button>
    </form>
  );
}

