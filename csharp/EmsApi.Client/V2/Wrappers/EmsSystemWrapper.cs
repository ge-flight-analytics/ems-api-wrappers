﻿using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using EmsApi.Client.V2.Model;

namespace EmsApi.Client.V2.Wrappers
{
    /// <summary>
    /// Provides a more natural .NET interface for the EMS API ems-system routes.
    /// </summary>
    public class EmsSystemWrapper : EmsApiRouteWrapper
    {
        /// <summary>
        /// Creates a new instance of the wrapper.
        /// </summary>
        /// <param name="api">
        /// The raw API interface to make calls to.
        /// </param>
        public EmsSystemWrapper( IEmsApi api ) : base( api ) { }

        /// <summary>
        /// Returns all EMS systems connected to the API endpoint that the user has access to.
        /// </summary>
        public Task<IEnumerable<EmsSystem>> GetAllAsync()
        {
            return ContinueWithExceptionSafety( api => api.GetEmsSystems() );
        }

        /// <summary>
        /// Returns all EMS systems connected to the API endpoint that the user has access to.
        /// </summary>
        public IEnumerable<EmsSystem> GetAll()
        {
            IEnumerable<EmsSystem> emsSystems = RethrowAggregateExceptions( GetAllAsync() );
            return EnsureEnumerableNotNull( emsSystems );
        }

        /// <summary>
        /// Returns a single EMS system that the user has access to. 
        /// </summary>
        /// <param name="id">
        /// The EMS system id to return.
        /// </param>
        public async Task<EmsSystem> GetAsync( int id )
        {
            var allSystems = await GetAllAsync();
            return allSystems.FirstOrDefault( ems => ems.Id == id );
        }

        /// <summary>
        /// Returns a single EMS system that the user has access to. 
        /// </summary>
        /// <param name="id">
        /// The EMS system id to return.
        /// </param>
        public EmsSystem Get( int id )
        {
            return GetAll().FirstOrDefault( ems => ems.Id == id );
        }

        /// <summary>
        /// Returns extended server properties for a single EMS system that the user has access to.
        /// </summary>
        /// <param name="id">
        /// The EMS system id to return information for.
        /// </param>
        public Task<EmsSystemInfo> GetSystemInfoAsync( int id )
        {
            return ContinueWithExceptionSafety( api => api.GetEmsSystemInfo( id ) );
        }

        /// <summary>
        /// Returns extended server properties for a single EMS system that the user has access to.
        /// </summary>
        /// <param name="id">
        /// The EMS system id to return information for.
        /// </param>
        public EmsSystemInfo GetSystemInfo( int id )
        {
            return RethrowAggregateExceptions( GetSystemInfoAsync( id ) );
        }

        /// <summary>
        /// Returns true if the EMS system is online.
        /// </summary>
        /// <param name="id">
        /// The EMS system id to check.
        /// </param>
        public Task<bool> PingAsync( int id )
        {
            return ContinueWithExceptionSafety( api => api.PingEmsSystem( id ) );
        }

        /// <summary>
        /// Returns true if the EMS system is online.
        /// </summary>
        /// <param name="id">
        /// The EMS system id to check.
        /// </param>
        public bool Ping( int id )
        {
            return RethrowAggregateExceptions( PingAsync( id ) );
        }
    }
}
