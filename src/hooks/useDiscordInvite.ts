import { useState, useEffect } from 'react';

export default function useDiscordInvite() {
  const [inviteUrl, setInviteUrl] = useState<string>('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch('/api/discord-invite')
      .then(response => response.json())
      .then(data => {
        setInviteUrl(data.invite_url);
        setLoading(false);
      })
      .catch(err => {
        setError('Failed to load Discord invite link');
        setLoading(false);
      });
  }, []);

  return { inviteUrl, loading, error };
}